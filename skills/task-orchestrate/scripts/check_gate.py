#!/usr/bin/env python3
"""Read-only local workflow gate checks; JSON allowed/reason, no next-action selection."""
import argparse
import json
import re
import subprocess
from pathlib import Path


class Blocked(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise Blocked(reason)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True, type=Path)
    parser.add_argument('--task', required=True)
    parser.add_argument('--head', required=True)
    actions = ('plan', 'review-plan', 'implement', 'review-implementation',
               'document', 'review-documentation', 'deliver', 'verify-delivery')
    parser.add_argument('--action', required=True, choices=actions)
    parser.add_argument('--state-at', help='Last note-bearing commit, only for verify-delivery')
    args = parser.parse_args()
    try:
        import yaml
    except ImportError:
        print(json.dumps({'allowed': False, 'reason': 'Missing PyYAML; install only with authorization'}))
        return 1

    # Reject duplicate mapping keys instead of silently trusting the last value.
    class Loader(yaml.SafeLoader):
        pass

    def mapping(loader, node):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node)
            require(isinstance(key, str) and key not in result, 'Invalid/duplicate YAML key')
            result[key] = loader.construct_object(value_node)
        return result

    Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    try:
        repo = args.repo.resolve(strict=True)

        def git(*commands, optional=False):
            process = subprocess.run(['git', '--no-optional-locks', '-c', f'safe.directory={repo.as_posix()}',
                                      '-C', str(repo), *commands], capture_output=True)
            if process.returncode:
                if optional:
                    return None
                raise Blocked('Git check failed: ' + ' '.join(commands[:2]))
            return process.stdout.decode('utf-8')

        def sha(value):
            require(isinstance(value, str) and bool(re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', value)),
                    'Commit references must be full lowercase SHAs')
            require(git('rev-parse', '--verify', value + '^{commit}').strip() == value,
                    'Reference is not a commit')
            return value

        def ancestor(left, right):
            return git('merge-base', '--is-ancestor', left, right, optional=True) is not None

        require(bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*-[0-9a-f]{8}', args.task)),
                'Invalid task ID')
        note = f'.task/{args.task}.md'
        require(Path(git('rev-parse', '--show-toplevel').strip()).resolve() == repo,
                '--repo must be the worktree root')
        head = sha(args.head)
        require(git('rev-parse', 'HEAD').strip() == head, 'HEAD differs from assignment')
        require(git('symbolic-ref', '--short', 'HEAD', optional=True) == f'task/{args.task}\n',
                'Branch differs from task identity')
        require(not git('status', '--porcelain', '--untracked-files=all'), 'Dirty handoff; reconcile first')

        def load(commit):
            text = git('show', f'{commit}:{note}', optional=True)
            require(text is not None, 'Task note missing at state reference')
            match = re.match(r'\A---\r?\n(.*?)\r?\n---\r?\n', text, re.S)
            require(match is not None, 'Task note needs YAML frontmatter')
            state = yaml.load(match[1], Loader=Loader)
            require(isinstance(state, dict), 'Task state must be a mapping')
            return state, text[match.end():]

        def block(body, name):
            start, end = f'<!-- task-{name}:start -->', f'<!-- task-{name}:end -->'
            require(body.count(start) == body.count(end) == 1 and body.index(start) < body.index(end),
                    f'Missing/ambiguous {name} block')
            return body.split(start, 1)[1].split(end, 1)[0]

        archived = args.action == 'verify-delivery'
        require(bool(args.state_at) == archived, '--state-at is required only for verify-delivery')
        state_at = sha(args.state_at) if archived else head
        require(ancestor(state_at, head), 'State reference is not an ancestor of HEAD')
        state, body = load(state_at)
        required = {'task', 'branch', 'base', 'stage', 'reviews', 'blocker', 'decision', 'recovery'}
        require(set(state) == required, 'Unexpected or missing task state fields')
        require(state['task'] == args.task and state['branch'] == f'task/{args.task}',
                'State identity differs from checkout')
        require(state['stage'] == ('deliver' if archived else args.action),
                'Requested action differs from recorded stage')
        base = sha(state['base'])
        require(ancestor(base, state_at), 'Base is not an ancestor of state')
        require(git('show', f'{base}:{note}', optional=True) is None, 'Task note existed at base')
        contract = block(body, 'contract')
        documentation = block(body, 'documentation')
        require(bool(contract.strip()), 'Contract block must contain the task requirements/plan')
        authors = {'review-plan': 'plan:', 'review-implementation': 'implement:',
                   'review-documentation': 'document:'}
        if args.action in authors:
            require(git('show', '-s', '--format=%s', head).startswith(authors[args.action]),
                    'Review dispatch requires its author handoff commit')
            if args.action == 'review-documentation':
                require(bool(documentation.strip()), 'Documentation assessment must be committed before review')
        for marker in ('decision', 'recovery'):
            require(state[marker] is None, f'Pending {marker}; normal progression blocked')
        blocker = state['blocker']
        if blocker is not None:
            require(isinstance(blocker, dict) and set(blocker) == {'id', 'attempts', 'evidence'},
                    'Malformed blocker')
            require(isinstance(blocker['id'], str) and bool(blocker['id']) and
                    type(blocker['attempts']) is int and blocker['attempts'] >= 0 and
                    isinstance(blocker['evidence'], list) and
                    all(isinstance(item, str) for item in blocker['evidence']), 'Malformed blocker fields')
            require(blocker['attempts'] < 2, 'Corrective-attempt limit reached')

        if archived:
            require(git('show', '-s', '--format=%P', head).split() == [state_at],
                    'Archived delivery must directly follow the last note commit')
            require(git('show', f'{head}:{note}', optional=True) is None, 'Delivery still contains task note')
            require(git('diff', '--name-only', state_at, head).splitlines() == [note],
                    'Changes after archived state are not only note removal')
            require(git('show', '-s', '--format=%s', head).startswith('deliver:'),
                    'Note removal needs a deliver: commit')
            require(not git('diff', '--name-only', base, head, '--', note), 'Task bookkeeping remains in final diff')

        reviews = state['reviews']
        require(isinstance(reviews, dict) and set(reviews) == {'plan', 'implementation', 'documentation'},
                'Expected all three review slots')
        prerequisites = {'plan': (), 'review-plan': (), 'implement': ('plan',),
                         'review-implementation': ('plan',), 'document': ('plan', 'implementation'),
                         'review-documentation': ('plan', 'implementation'),
                         'deliver': tuple(reviews), 'verify-delivery': tuple(reviews)}
        prefixes = {'plan': 'review-plan:', 'implementation': 'review-implementation:',
                    'documentation': 'review-documentation:'}
        upstream = {'plan': (), 'implementation': ('plan',),
                    'documentation': ('plan', 'implementation')}
        receipts = {}

        def object_at(commit, path):
            entry = git('ls-tree', commit, '--', path).strip()
            require(not entry or entry.split()[1] == 'blob', 'Assessed artifacts must be files')
            return entry

        for gate in ('plan', 'implementation', 'documentation'):
            record = reviews[gate]
            if record is None:
                require(gate not in prerequisites[args.action], f'Missing {gate} review')
                continue
            require(isinstance(record, dict) and set(record) == {'verdict', 'input', 'artifacts'},
                    f'Malformed {gate} review')
            require(record['verdict'] in ('pass', 'revise', 'needs-decision'), 'Invalid review verdict')
            reviewed = sha(record['input'])
            require(ancestor(base, reviewed) and ancestor(reviewed, state_at), 'Review input outside task history')
            paths = record['artifacts']
            require(isinstance(paths, list) and all(isinstance(p, str) for p in paths) and
                    len(paths) == len(set(paths)), 'Malformed assessed paths')
            for path in paths:
                require(path and not path.startswith('/') and '\\' not in path and ':' not in path and
                        all(part not in ('', '.', '..') for part in path.split('/')) and
                        not any(char in path for char in '*?[') and path != note,
                        'Use literal repository-relative artifact paths, not the task note')
                require(object_at(reviewed, path) or object_at(base, path), 'Assessed file never existed')
            # Findings commit is discoverable in history: no self-SHA or execution array.
            receipt = False
            for commit in git('log', '--format=%H', f'{base}..{state_at}', '--', note).splitlines():
                if not git('show', '-s', '--format=%s', commit).startswith(prefixes[gate]):
                    continue
                parents = git('show', '-s', '--format=%P', commit).split()
                require(parents == [reviewed], f'{gate} review lacks the latest matching findings commit')
                require(git('diff', '--name-only', reviewed, commit).splitlines() == [note],
                        'Reviewer findings commit must change only the task note')
                recorded, _ = load(commit)
                historic_reviews = recorded.get('reviews')
                require(isinstance(historic_reviews, dict), 'Malformed historical review mapping')
                if historic_reviews.get(gate) == record:
                    receipt = True
                    receipts[gate] = commit
                break
            require(receipt, f'{gate} review lacks a matching findings commit')
            if gate not in prerequisites[args.action]:
                continue
            require(record['verdict'] == 'pass', f'{gate} review has not passed')
            reviewed_state, reviewed_body = load(reviewed)
            review_action = prefixes[gate].removesuffix(':')
            require(reviewed_state.get('stage') == review_action and
                    git('show', '-s', '--format=%s', reviewed).startswith(authors[review_action]),
                    f'{gate} review input is not its author handoff')
            if gate == 'documentation':
                require(bool(block(reviewed_body, 'documentation').strip()),
                        'Documentation review lacks a committed assessment')
            reviewed_reviews = reviewed_state.get('reviews')
            require(isinstance(reviewed_reviews, dict), 'Malformed reviewed prerequisite mapping')
            for prior in upstream[gate]:
                require(reviewed_reviews.get(prior) == reviews[prior] and
                        prior in receipts and ancestor(receipts[prior], reviewed),
                        f'{gate} review predates the current {prior} approval')
            require(block(reviewed_body, 'contract') == contract, f'{gate} contract assessment is stale')
            if gate == 'documentation':
                require(block(reviewed_body, 'documentation') == documentation, 'Documentation assessment is stale')
            for path in paths:
                require(object_at(reviewed, path) == object_at(head, path), f'{gate} artifact changed: {path}')
        if args.action in ('deliver', 'verify-delivery'):
            require(blocker is None, 'Unresolved blocker prevents delivery')
        print(json.dumps({'allowed': True, 'reason': 'Local prerequisites satisfied; agent/host judgments still required'}))
        return 0
    except (Blocked, OSError, UnicodeError, ValueError, TypeError, yaml.YAMLError) as error:
        print(json.dumps({'allowed': False, 'reason': str(error)}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())

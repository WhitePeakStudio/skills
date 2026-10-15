"""Render Copilot agent profiles from shared guidance and compact role definitions."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def render(root=ROOT, check=False):
    guidance = (root / 'studio.whitepeak/organization.md').read_text(encoding='utf-8').strip()
    definitions = json.loads((root / 'studio.whitepeak/agents.json').read_text(encoding='utf-8'))
    if not guidance or not isinstance(definitions, dict) or not definitions:
        raise ValueError('Shared guidance and agent definitions must be nonempty')
    output = root / 'com.github.copilot/agents'
    expected = {}
    for name, definition in definitions.items():
        if (not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name)
                or set(definition) - {'description', 'prompt', 'model'}
                or not all(isinstance(definition.get(key), str) and definition[key].strip()
                           for key in ('description', 'prompt'))):
            raise ValueError(f'Invalid agent definition: {name}')
        skill = 'issue-execute' if name == 'generic' else name
        if not (root / 'skills' / skill / 'SKILL.md').is_file():
            raise ValueError(f'Missing skill for {name}')
        header = {'name': name, 'description': definition['description']}
        if 'model' in definition:
            if not isinstance(definition['model'], str) or not definition['model'].strip():
                raise ValueError(f'Invalid Copilot model: {name}')
            header['model'] = definition['model']
        if name not in {'generic', 'task-orchestrate'}:
            header['user-invocable'] = False
        # JSON is a YAML subset; no extra dependency is needed to produce frontmatter.
        expected[name + '.agent.md'] = ('---\n' + json.dumps(header, indent=2) + '\n---\n\n'
            + guidance + '\n\n' + definition['prompt'].strip() + '\n')
    existing = {p.name for p in output.glob('*.agent.md')}
    if existing - expected.keys():
        raise ValueError('Unexpected profiles; remove or reconcile them explicitly')
    for name, content in expected.items():
        path = output / name
        if check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                raise ValueError(f'Stale generated profile: {name}; run scripts/build-agents.py')
        else:
            output.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')
    print(f'{len(expected)} agent profiles {"verified" if check else "generated"}.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    render(check=parser.parse_args().check)

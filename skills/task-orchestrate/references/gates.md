# Workflow gates

Run the read-only [checker](../scripts/check_gate.py) before normal role dispatch
and delivery. It needs Python 3.10+, Git, and PyYAML (install only with authorization:
`python -m pip install PyYAML`). It returns only `allowed` and `reason`; exit 0
permits the requested local action, exit 1 blocks it, exit 2 is CLI misuse.
It never edits, commits, dispatches, contacts a remote, or approves hosted checks.

```sh
python /path/to/check_gate.py --repo /path/to/worktree --task example-a1b2c3d4 --head <full-sha> --action implement
```

## Transitions

`stage` names the next action, not the role currently writing. Authors commit
before marking their review ready; reviewers commit their findings and next stage.
Role Status and review verdict remain separate. Apply the following rules together;
any unmatched result or inconsistent state blocks progression, never skips a gate.

| Completed action | Successful result → next stage | Correction → next stage |
|---|---|---|
| plan | Committed plan → review-plan | Incomplete plan → plan |
| review-plan | pass → implement | revise → plan |
| implement | Committed implementation → review-implementation | Implementation correction → implement; contract/scope issue → plan |
| review-implementation | pass → document | Code findings → implement; contract/scope findings → plan |
| document | Committed docs or no-change decision → review-documentation | Documentation correction → document; code issue → implement; contract/scope issue → plan |
| review-documentation | pass with all gates valid → deliver | Documentation findings → document; code issue → implement; contract/scope issue → plan |
| deliver | PR opened → verify-delivery | Push/creation/attachment failure → deliver; substantive edits → responsible author |
| verify-delivery | Applicable checks pass, mergeability established → complete | Failed checks → responsible author; integration conflict → resolution then affected author/reviews |
| complete | Terminal | New changes → affected author/reviews |

For any review, `revise` routes by finding type as above; `needs-decision` uses the
decision rule below. A review cannot pass with unresolved blockers. Upstream returns
require the normal author/review sequence before downstream work resumes, including
fresh documentation after code/contract correction.

| Condition at any stage | Required behavior |
|---|---|
| Missing/stale prerequisite review | Block dependent action; restore the affected author/review gate |
| Material decision unavailable | Record decision; pause dependent actions; resume interrupted stage after resolution |
| Interrupted writer, dirty checkout, wrong branch/HEAD | Block normal dispatch; reconcile through explicit recovery |
| Same blocker survives two corrective attempts without new evidence | Stop and report; no automatic third attempt |
| Pending/unknown hosted checks or mergeability | Remain verify-delivery, report pending, retain worktree |
| Unmatched result/inconsistent state | Block and reconcile |

When a paused review resumes after a decision or bookkeeping commit, obtain a new
author handoff before fresh review; do not review an orchestrator's note-only commit.

An author may remain at its stage while work is incomplete. A no-change documentation
result still needs its own committed assessment and independent review. No automatic
merge/rebase, monitoring, retries after the stopping limit, or weakening of gates.

## Current state

Use YAML frontmatter in the existing `.task/<id>.md`. No execution array or separate
report: replace current records; Git commits retain every prior attempt and pass.

```yaml
---
task: example-a1b2c3d4
branch: task/example-a1b2c3d4
base: <full-base-sha>
stage: plan
reviews:
  plan: null
  implementation: null
  documentation: null
blocker: null
decision: null
recovery: null
---
```

Each latest review is `{verdict: pass|revise|needs-decision, input: <full-sha>,
artifacts: [literal/repository-relative/files]}`. `input` is the reviewer's assigned
HEAD, not its findings commit. The reviewer commits immediately on that HEAD with
its `review-…:` prefix; Git supplies the findings commit without a self-referencing
SHA field. `artifacts` lists files whose unchanged contents preserve approval,
not every file consulted. Typical selections:

- Plan: affected specifications and stable constraints.
- Implementation: implementation/tests and contract dependencies.
- Documentation: documentation and the code/specifications supporting its claims.

Treat planned downstream edit targets as context unless approval depends on their
current contents. If it does, include them and rerun the affected gate after changes;
never exclude a required dependency merely to keep a pass valid. Keep paths precise
and include additions/deletions. Empty lists are valid only for an
evidenced no-file-change assessment. The checker cannot prove scope completeness
or reviewer identity/correctness; reviewers remain responsible for those judgments.

Put objective, scope, acceptance, plan, and authoritative references between
`<!-- task-contract:start -->` and `<!-- task-contract:end -->`. Put documentation
assessment/no-change rationale between `<!-- task-documentation:start -->` and
`<!-- task-documentation:end -->` (initially empty). Keep evidence, findings, stage
details, and model selections outside those blocks. Compare block text exactly;
even whitespace edits require reassessment. Bookkeeping outside them does not.

All gates assess the contract block; documentation also assesses the documentation
block. Other assessed files are compared by Git object and mode at the reviewed SHA
and current HEAD. Unchanged descendants preserve passes; relevant changes invalidate
the affected gate and downstream gates. Clear downstream records when upstream
correction is required; keep valid unaffected records. A new review replaces its
own latest record; authors never manufacture review passes.
Downstream review inputs must retain the current upstream approval records and
descend from their findings commits. Renewed upstream approvals therefore require
fresh downstream reviews; a restored file alone cannot bypass that sequence.

An active blocker is `{id: stable-name, attempts: 0, evidence: [references]}`.
Increment attempts only after a corrective attempt leaves that blocker unresolved.
Do not reset by renaming it or changing stages. Agent judgment establishes blocker
identity and materially new evidence; record why before resetting the count when
new evidence changes the correction basis. Resolve the blocker to null when fixed.
`decision` is null or the material question; `recovery` is null or the interrupted
role name. Both non-null markers block normal progression. Explicit recovery follows
the shared protocol, outside normal checker permission, and clears its marker only
after reconciliation and a clean committed handoff.

The checker requires current `stage` to match `--action`, branch/task identity,
exact HEAD, clean tracked/untracked status, committed state, ancestor references,
review provenance in Git history, and valid prerequisite passes. Planning/review-plan
need no earlier pass; implementation/review-implementation need plan; documentation/
review-documentation need plan+implementation; delivery needs all three.
Review dispatch and passing review inputs must be the corresponding author's
handoff commit (`plan:`, `implement:`, `document:`), with stage set to that review.
Documentation assessment must be nonempty even for no-change tasks. This checks
commit provenance, not authorship identity or assessment quality.

## Delivery and resume

Run `--action deliver` before removing the note. Keep the last note-bearing commit
SHA in the delivery return/PR evidence. For local verification after note removal:

```sh
python /path/to/check_gate.py --repo /path/to/worktree --task example-a1b2c3d4 --head <delivery-sha> --action verify-delivery --state-at <last-note-sha>
```

Archived state must say `deliver`; HEAD must directly follow it with only the note
deletion, a `deliver:` subject, and all passes still valid.
This permits inspection of hosted delivery, not a claim that CI passed or a PR exists.
The orchestrator fetches target, inspects hosted status, reports pending/failure,
and decides completion under the shared delivery rules. Keep pending external state
in the delivery return/PR evidence; do not restore bookkeeping merely to record it.
If role work resumes, restore the note from history, update stage/blockers/reviews,
commit, rerun applicable gates, and remove the note again before pushing.

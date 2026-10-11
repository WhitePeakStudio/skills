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


State and receipt details: [state.md](state.md).
Delivery and archived verification: [delivery.md](delivery.md).

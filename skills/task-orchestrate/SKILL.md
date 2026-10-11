---
name: task-orchestrate
description: Coordinate a repository task through isolated worktrees, fresh-context planning and review roles, implementation review, and pull-request delivery.
---

# Orchestrate a repository task

Own the lifecycle; delegate role work to [task-plan](../task-plan/SKILL.md),
[task-review-plan](../task-review-plan/SKILL.md),
[task-implement](../task-implement/SKILL.md), and
[task-review-implementation](../task-review-implementation/SKILL.md).
This workflow requires subagents that can start without inherited conversation
history and a Git repository. If unavailable, report that limitation; do not
claim independent review or an isolated Git workflow.

## Isolation and state

Inspect repository instructions and the user's scope and delivery authorization.
Resolve the user's target branch, otherwise the remote default branch, and its
current commit as the base. If unresolved, ask before creating the worktree.
Choose `<id>` as `<short-kebab-slug>-<8-random-hex>`. Create branch `task/<id>`
and one worktree in sibling `<repo>-tasks/<id>` from that base commit.
Check branch, path, and note collisions before creation, then verify the resulting
checkout, branch, and HEAD. Never reuse another task's mutable checkout.
Independent tasks may run concurrently in separate worktrees; roles within one
task run sequentially.

Create and commit one `.task/<id>.md` note containing objective, scope, source
references, acceptance, base commit, current plan/stage, latest findings/evidence,
and decisions/open issues. Confirm the note path was absent at the base. Keep the
note compact: replace stale state rather than appending transcripts or reports.
Repository files and the note provide context without inherited chat history.

## Role protocol

Each assignment names the role skill and supplies only the absolute worktree,
branch, objective/scope, exact input commit, source references, acceptance, and
expected result. Start a fresh-context subagent (for example `fork_turns="none"`)
and wait for its completion and commit before dispatching the next role. Do not
send routine progress chatter or another role's reasoning transcript.

Before any write, every role verifies its working path, branch, empty tracked and
untracked status, and HEAD equal to the assigned input SHA. A mismatch or dirty
handoff stops for reconciliation; preserve changes without reset, deletion, or
automatic attribution to unrelated work. Follow repository instructions and
inspect only the sources needed for the assignment.

Planner and reviewers write only the task note. Implementer may change authorized
code/documentation and that note. Each role updates current state, stages only
its authorized files, and commits before returning. Preserve configured signing;
verify the resulting commit and clean status. Role subagents never push or open
PRs. Return only `Status`, `Commit`, `Result`, `Evidence`, and `Open issues`.
Status describes assignment completion (`complete`, `blocked`, or
`needs-decision`); it is separate
from a review verdict (`pass`, `revise`, or `needs-decision`) in Result and the
note. Reviewers record the exact reviewed input SHA separately from their own
later note commit. A pass never implicitly approves subsequent changes.
Use commit subject prefixes `plan:`, `review-plan:`, `implement:`, and
`review-implementation:` for the corresponding roles.

## Gates and corrections

Dispatch planner, then plan reviewer against the planner's exact commit. Proceed
to implementation only with a passing plan review. Dispatch implementer against
the latest clean note commit, then implementation reviewer against the exact
implementation commit. The review's note commit becomes the next handoff HEAD;
the approved artifact remains the recorded reviewed SHA.

Blocking findings produce `revise`: return to the corresponding author, then
request a fresh review of the corrective commit. Plan corrections go to planner
and plan reviewer; implementation corrections go to implementer and implementation
reviewer. A scope or plan change re-enters the plan/review gate before dependent
implementation. Advisories do not block a pass when their disposition is recorded.

Missing material decisions produce `needs-decision`: record the question and ask
the user, continuing independent authorized work while dependent work waits.
Never infer approval from elapsed time. If the same blocker survives two
corrective attempts with no new evidence, stop that loop, preserve the attempts
and evidence in the note, and return the unresolved issue.

## Delivery

Default delivery is a PR; respect any user-directed alternative. Before external
actions, establish required authorization under the active host rules. After a
passing implementation review, remove `.task/<id>.md` in a `deliver:` commit.
Preserve all role commits. Verify clean status, the note's absence at base and
delivery, and zero base-to-delivery net diff for that path. Recheck that delivery
changes only bookkeeping; substantive edits require a fresh implementation review.

Push the explicit task branch without force, leaving the base branch unchanged,
and create a PR targeting the resolved target branch, describing behavior and
actual validation.
Attach the created PR when the host requires it. Remove only the clean task
worktree, and only after successful PR creation and required attachment; retain
the branch and commit history. Failed push, PR creation/attachment, or dirty
cleanup retains recoverable checkout/branch state and reports the failure.
Distinguish disposable/local simulations from a live hosted PR and report only
checks actually performed.

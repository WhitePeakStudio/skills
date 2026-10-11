---
name: task-review-plan
description: Independently review an exact task-plan commit for feasibility, scope, acceptance, and unresolved decisions, recording a verdict in the task note.
---

# Review a plan

Read only the [shared role protocol](../task-orchestrate/SKILL.md#role-protocol)
and assigned sources; unrelated orchestrator sections are unnecessary. Before
writing, verify the assigned absolute path, branch, clean tracked/untracked
status, and HEAD equal to the input SHA; stop on mismatch, preserving changes.

Review the plan at that exact input commit against objective, scope, repository
constraints, acceptance, verification, risks, and material decisions. Check that
prior blocking findings were corrected and advisories have a disposition. Do not
rewrite the plan or silently expand scope.

Write only `.task/<id>.md`: record reviewed input SHA, actionable findings and
evidence, and verdict `pass`, `revise`, or `needs-decision`. Blocking findings
require correction and fresh review; accounted-for advisories do not block a pass.
Missing material decisions require a recorded question, without assumed approval.
Replace stale review state while retaining current plan and relevant decisions.

Commit the note and verify clean status. Return `Status`, `Commit`, `Result`,
`Evidence`, `Open issues`; Result carries the verdict. Assignment completion is
separate from acceptance. Commit is your later note commit, not the reviewed
input SHA. A pass applies only to that input; corrections require another review.
Do not implement, push, or create a PR.

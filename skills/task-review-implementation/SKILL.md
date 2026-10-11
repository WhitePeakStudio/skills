---
name: task-review-implementation
description: Independently review an exact implementation commit against its accepted task plan and acceptance criteria, committing findings and a verdict only in the task note.
---

# Review an implementation

Read only the [shared role protocol](../task-orchestrate/SKILL.md#role-protocol)
and assigned sources; unrelated orchestrator sections are unnecessary. Before
writing, verify the assigned absolute path, branch, clean tracked/untracked
status, and HEAD equal to the input SHA; stop on mismatch, preserving changes.

Inspect that exact implementation commit and its diff against the accepted plan,
scope, acceptance, and repository constraints. Assess correctness, regressions,
and verification evidence; run focused read-only checks where useful. Check
prior blocking findings and advisory dispositions. Do not silently fix code or
approve a changed plan; scope/plan changes require the plan/review gate.

Write only `.task/<id>.md`: record reviewed input SHA, actionable findings,
evidence/limitations, and verdict `pass`, `revise`, or `needs-decision`. Blocking
findings require correction and fresh review; accounted-for advisories do not
block a pass. Record missing material decisions without assuming approval.
Replace stale review state while retaining current plan and relevant decisions.

Commit the note, verify clean status, and return `Status`, `Commit`, `Result`,
`Evidence`, `Open issues`; Result carries the verdict. Assignment completion is
separate from acceptance. Commit is your later note commit, not the reviewed
input SHA. A pass applies only to that input; corrections require another review.
Do not push or create a PR.

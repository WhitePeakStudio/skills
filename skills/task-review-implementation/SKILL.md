---
name: task-review-implementation
description: Independently review an exact implementation commit against accepted planning, authoritative specifications, acceptance, and verification evidence.
---

# Review an implementation

Read the [shared role protocol](../task-orchestrate/SKILL.md#role-protocol) and
[gate rules](../task-orchestrate/SKILL.md#gates-and-corrections). Verify assigned
path, branch, clean tracked/untracked status, and exact input HEAD before writing;
stop on mismatch, preserving changes.

Check the recorded plan pass against its exact reviewed reference and current
assessed artifacts. Inspect the assigned implementation and diff against accepted
plan/specifications, scope, acceptance, and constraints. Assess correctness,
regressions, and verification evidence, including capability/rule coverage;
run focused read-only checks where useful. Check prior blocking findings and
advisory dispositions. Do not silently fix code or approve changed contracts/plans;
route those changes to planner and plan reviewer before dependent implementation.

Write only `.task/<id>.md`: record verdict `pass`, `revise`, or `needs-decision`,
exact reviewed input SHA, assessed implementation/tests and accepted references,
actionable findings, evidence, and limitations. Preserve the plan review record
and relevant decisions; mark downstream documentation assessments pending or
invalid when affected. Blocking findings require implementation correction and
fresh review; accounted-for advisories do not block a pass. Record missing
material decisions without assuming approval.

Commit with `review-implementation:`, verify clean status, and return the shared
five fields; Result carries the verdict. Completion is separate from acceptance;
your note commit is distinct from reviewed input. Descendants retain a pass only
under shared artifact-validity rules. A pass makes the task ready for mandatory
documentation and its review, including a no-change decision. Do not push or open a PR.

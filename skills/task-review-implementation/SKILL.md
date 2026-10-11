---
name: task-review-implementation
description: Independently review an exact implementation commit against accepted planning, authoritative specifications, acceptance, and verification evidence.
---

# Review an implementation

Read and follow the [shared role protocol](../task-orchestrate/SKILL.md#role-protocol)
and [gate rules](../task-orchestrate/SKILL.md#gates-and-corrections). Before writing,
verify path, branch, clean tracked/untracked status, and exact input HEAD; stop on
mismatch, preserving changes. Only explicit recovery assignments waive clean input.

Validate the plan pass against its exact reviewed reference and current artifacts.
Review cumulative implementation changes from task base to input SHA against
accepted plan/specs, scope, acceptance, and constraints, not only the latest correction.
Assess correctness, regressions, verification evidence, and capability/rule coverage;
run useful focused read-only checks. Check prior blockers/advisory dispositions.
Never fix code or approve changed contracts/plans; route them to planner/reviewer
before dependent implementation.

Write only `.task/<id>.md`: verdict `pass`, `revise`, or `needs-decision`, exact
reviewed SHA, assessed implementation/tests, accepted references, actionable findings,
evidence/limits. Preserve plan review/decisions; mark downstream documentation pending
or invalid when affected. Blockers require correction/fresh review; accounted-for
advisories do not block. Record missing decisions without assumed approval.

Commit with `review-implementation:`, verify clean status, and return the shared
five fields with verdict in Result. Completion differs from acceptance; your note
commit differs from reviewed input. Descendant passes follow shared validity rules.
A pass permits mandatory documentation/review, including no-change decisions.
Do not push or open a PR.

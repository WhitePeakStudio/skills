---
name: task-implement
description: Implement an independently accepted task plan and authoritative specifications, changing authorized implementation and tests before independent review.
---

# Implement a task

Read and follow the [shared role protocol](../task-orchestrate/SKILL.md#role-protocol)
and [gate rules](../task-orchestrate/SKILL.md#gates-and-corrections). Before writing,
verify path, branch, clean tracked/untracked status, and exact input HEAD; stop on
mismatch, preserving changes. Only explicit recovery assignments waive clean input.

Validate the note's plan pass against its exact reviewed reference and current
plan/spec artifacts. Implement within accepted plan, contracts, scope, and repository
instructions. Reference capability paths/rule names in verification. Resolve blocking
implementation findings and record advisory dispositions. Scope/plan/contract changes
return to planner/reviewer before dependent implementation; record discrepancies and
missing decisions, continuing only independent authorized work.

Write only authorized implementation/tests and `.task/<id>.md`, not specs or later
documentation. Classify actual purpose/content: SKILL.md product instructions can
be implementation. Run checks appropriate to acceptance/changes. Record stage,
evidence, limitations, and open issues, distinguishing simulations/live checks.
Preserve accepted reviews; mark implementation/downstream gates pending or invalid
as appropriate. Never claim a review verdict for your own work.

Commit with `implement:`, verify clean status, and return the shared five fields.
Mark ready for independent review at this exact commit; its pass permits mandatory
documentation and review. Do not push or open a PR.

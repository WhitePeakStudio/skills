---
name: task-implement
description: Implement an independently accepted task plan and authoritative specifications, changing authorized implementation and tests before independent review.
---

# Implement a task

Read the [shared role protocol](../task-orchestrate/SKILL.md#role-protocol) and
[gate rules](../task-orchestrate/SKILL.md#gates-and-corrections). Verify assigned
path, branch, clean tracked/untracked status, and exact input HEAD before writing;
stop on mismatch and preserve changes.

Confirm the note's passing plan review remains valid against the current plan
and specifications by comparing its exact reviewed reference and assessed
artifacts. Implement within that accepted plan, contracts, scope, and repository
instructions. Reference capability paths and rule names in relevant verification.
On correction, resolve blocking implementation findings and record advisory
dispositions. If scope, plan, or contract must change, record the discrepancy and
return to planner/plan reviewer before dependent implementation. Record missing
material decisions, continuing only independent authorized work.

Change only authorized implementation/tests and `.task/<id>.md`; do not edit
specifications or perform the later documentation stage. Classify sources by
purpose/content: a SKILL.md product instruction can be implementation. Run checks
appropriate to acceptance and actual changes. Update stage, evidence, limitations,
and open issues; distinguish simulations from live checks. Preserve accepted
review references and mark the implementation/downstream assessments pending or
invalid as appropriate. Do not claim a reviewer verdict for your own work.

Commit with `implement:`, verify clean status, and return the shared five fields.
Mark ready for independent implementation review of this exact commit.
Documentation follows its passing review on every task. Do not push or open a PR.

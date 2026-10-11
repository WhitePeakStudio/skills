---
name: task-plan
description: Plan or correct a repository task by writing affected authoritative specifications and a compact task note before independent plan review.
---

# Plan a task

Read the [shared role protocol](../task-orchestrate/SKILL.md#role-protocol) and
[gate rules](../task-orchestrate/SKILL.md#gates-and-corrections). Verify assigned
path, branch, clean tracked/untracked status, and exact input HEAD before writing;
stop on mismatch and preserve changes.

Inspect objective, repository constraints, acceptance, related contracts, and note.
Use [specbook](../specbook/SKILL.md) to create or update affected capability files
in `spec/`, including required index links. If structures are missing, create only
useful content needed for this task; no empty scaffolds or unrelated migration.
Keep implementation plans and decision history in the note, outside contracts.
Link task acceptance and planned verification to capability paths and rule names;
record a reason when the task needs no contract change rather than inventing one.

Write a feasible plan, verification, material risks, and required decisions in
`.task/<id>.md`. On correction, resolve blocking findings and record advisory
dispositions. Preserve acceptance, decisions, evidence, and earlier review
references; mark affected gates invalid when their assessed artifacts changed.
Record missing material decisions and pause dependent work without inventing an
answer; continue independent authorized planning.

Write only affected specifications and note. Commit with `plan:`, verify clean
status, and return the shared five fields. Mark ready for plan review; your revision
is not an accepted review. Do not implement, document, push, or open a PR.

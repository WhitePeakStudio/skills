---
name: task-plan
description: Plan or correct a repository task by writing affected authoritative specifications and a compact task note before independent plan review.
---

# Plan a task

Read the [role contract](../task-orchestrate/references/role-contract.md) and
[note state](../task-orchestrate/references/state.md); load only relevant artifacts
and conditional references. Follow their handoff, freshness, and correction rules.

Inspect objective, constraints, acceptance, related contracts, and note. Use
[specbook](../specbook/SKILL.md) for affected `spec/` capabilities and required index
links. Create only useful missing content; no empty scaffolds or unrelated migrations.
Keep implementation plans/decision history in the note, outside contracts. Link
acceptance/verification to capability paths/rule names; justify no-contract-change
decisions rather than inventing contracts.

Write feasible plan, verification, material risks, and decisions in `.task/<id>.md`.
Resolve blocking findings and record advisory dispositions. Preserve acceptance,
decisions, evidence, and earlier reviews; invalidate gates whose assessed artifacts
changed. Record missing material decisions; pause dependent work without inventing
answers, continuing independent authorized planning.

Write only affected specs and note. Commit with `plan:`, verify clean status, and
return the shared five fields. Mark ready for plan review, not self-accepted.
Do not implement, document, push, or open a PR.

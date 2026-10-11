---
name: task-plan
description: Plan or correct a repository task as a fresh-context planning role, committing only its task note before independent plan review.
---

# Plan a task

Read only the [shared role protocol](../task-orchestrate/SKILL.md#role-protocol)
and assigned sources; unrelated orchestrator sections are unnecessary. Apply its
compact assignment/return contract. Before writing, verify the assigned absolute
path, branch, clean tracked/untracked status, and HEAD equal to the input SHA;
stop on mismatch and preserve existing changes.

Inspect the objective, repository constraints, acceptance, and current task note.
Write a feasible implementation plan with verification, material risks, and any
required decisions. Keep steps concrete enough to implement and review without
turning the note into a design report. On correction, address blocking findings
and record advisory dispositions; do not treat your revision as reviewed.

Write only `.task/<id>.md`. Replace stale plan/stage/findings while preserving
current scope, acceptance, decisions, and relevant evidence. Record missing
material decisions and pause dependent work; perform independent authorized
planning without inventing an answer.

Commit the note, verify clean status, and return `Status`, `Commit`, `Result`,
`Evidence`, `Open issues`. Mark the stage ready for plan review; completion of
this assignment does not approve the plan. Do not implement, push, or create a PR.

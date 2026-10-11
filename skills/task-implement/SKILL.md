---
name: task-implement
description: Implement an independently accepted repository task plan or corrective findings in an assigned isolated worktree, then commit changes and verification evidence.
---

# Implement a task

Read only the [shared role protocol](../task-orchestrate/SKILL.md#role-protocol)
and assigned sources; unrelated orchestrator sections are unnecessary. Before
writing, verify the assigned absolute path, branch, clean tracked/untracked
status, and HEAD equal to the input SHA; stop on mismatch, preserving changes.

Confirm the task note records a passing review of the current plan's exact
commit. Implement within that plan, scope, repository instructions, and acceptance.
On correction, address blocking implementation findings and record advisory
dispositions. If a scope or plan change is needed, record it and return for the
plan/review gate before dependent implementation. Record missing material
decisions, continuing only independent authorized work.

Change only authorized code/documentation and `.task/<id>.md`. Run checks
appropriate to acceptance and actual changes. Replace stale implementation
stage/findings with results, evidence, limitations, and open issues; distinguish
simulations from live checks. Do not claim a reviewer verdict for your own work.

Commit authorized changes and the note, verify clean status, and return `Status`,
`Commit`, `Result`, `Evidence`, `Open issues`. Mark the stage ready for independent
implementation review of this exact commit. Do not push or create a PR.

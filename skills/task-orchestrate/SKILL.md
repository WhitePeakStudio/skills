---
name: task-orchestrate
description: Coordinate isolated repository tasks through specification planning, implementation, documentation, three independent review gates, and pull-request delivery.
---

# Orchestrate a repository task

Require Git and fresh-context subagents; report missing capabilities without
claiming isolation or independent review. Own lifecycle and state; roles write
sequentially in one isolated task worktree.
For an explicit issue URL, read [issue handoff](references/issues.md) before
creating/resuming work and apply it through delivery. Direct task requests do
not load it; Ready permits planning, not skipping any review gate.
Read the [role contract](references/role-contract.md), [note state](references/state.md),
and [gate transitions/checker](references/gates.md). Run the read-only checker before
normal dispatch and delivery; denial blocks that action. The checker proves local
prerequisites, not review correctness or hosted verification.

Dispatch these roles in order, using their SKILL.md paths as assignment sources:
[plan](../task-plan/SKILL.md), [review plan](../task-review-plan/SKILL.md),
[implement](../task-implement/SKILL.md), [review implementation](../task-review-implementation/SKILL.md),
[document](../task-document/SKILL.md), [review documentation](../task-review-documentation/SKILL.md).
All three reviews are required, including documentation no-change decisions.
Let each subagent load its role and relevant artifacts/specialist skill; do not
load every role, specialist, or checker source into the orchestrator by default.

## Subagent models


Explicit task instructions override preferences globally/per role; unspecified roles retain them.

| Roles | Preferred model |
|---|---|
| task-document, task-review-documentation | GPT-6 Luna (`gpt-6-luna`) |
| task-plan, task-review-plan, task-implement, task-review-implementation | GPT-6.1 Sol (`gpt-6.1-sol`) |

Validate advertised model/effort controls before dispatch. Use documented IDs for
the same model; never guess aliases or provider equivalents. Unavailable built-in
preferences/selection controls inherit the harness default with disclosure.
Unsupported explicit models/efforts require a decision before dependent dispatch.
Inherit unspecified effort. Keep choices stable across corrections unless instructed;
record actual selections/fallbacks once in the model map, marking unknown actual models.
Apply settings through harness controls, not agent prompts. This mapping neither
selects the orchestrator model nor waives fresh context.

## Isolation and dispatch

Inspect repository instructions, scope, and delivery authorization. Resolve the
requested target branch, otherwise the remote default, and its current base
commit; ask if unresolved. Choose `<id>` as `<short-kebab-slug>-<8-random-hex>`.
Check branch/worktree/note collisions, then create `task/<id>` and sibling
`<repo>-tasks/<id>` from base. Verify path, branch, HEAD, and note absence at base.
Never reuse another task's mutable checkout. Different task worktrees may run
concurrently; each has one active role writer. Never overwrite unrelated changes,
force-push, or delete dirty worktrees.

Commit the initial `.task/<id>.md` and model map. Dispatch under the role contract
with fresh contexts (e.g. `fork_turns="none"`). Check note freshness alongside the
mechanical gate before accepting/dispatching; return inconsistencies to the writer.
Wait for its clean committed return before the next dispatch. Read additional
detail only to resolve an issue.

Follow the gate transitions and correction rules. Do not integrate target
advancement automatically; integration changes reopen affected gates.

Read [recovery](references/recovery.md) only for interrupted/dirty/mismatched
handoffs; confirm writers and children stopped before reconciliation. Read
[delivery](references/delivery.md) when all gates pass, or when resuming delivery.

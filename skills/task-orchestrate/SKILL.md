---
name: task-orchestrate
description: Coordinate isolated repository tasks through specification planning, implementation, documentation, three independent review gates, and pull-request delivery.
---

# Orchestrate a repository task

Own the lifecycle; delegate sequentially to [task-plan](../task-plan/SKILL.md),
[task-review-plan](../task-review-plan/SKILL.md),
[task-implement](../task-implement/SKILL.md),
[task-review-implementation](../task-review-implementation/SKILL.md),
[task-document](../task-document/SKILL.md), and
[task-review-documentation](../task-review-documentation/SKILL.md).
Require Git and fresh-context subagents; report missing capabilities without
claiming isolation or independent review.
Read and follow the [gate contract](references/gates.md): exhaustive transitions,
compact YAML state, bounded assessment blocks, and read-only checker invocation.
Run its checker before normal dispatch and delivery; a denial blocks that action.
The checker does not choose corrective routes or establish review/hosted correctness.

## Subagent models

Explicit task instructions override these preferences globally or per role;
unspecified roles retain them.

| Roles | Preferred model |
|---|---|
| task-document, task-review-documentation | GPT-6 Luna (`gpt-6-luna`) |
| task-plan, task-review-plan, task-implement, task-review-implementation | GPT-6.1 Sol (`gpt-6.1-sol`) |

Before dispatch, validate model and effort through advertised harness controls.
Use documented identifiers for the same model; never guess aliases or other-provider
equivalents. Unavailable built-in preferences or unsupported selection controls
inherit the harness default with disclosure; unsupported explicit models or efforts
require a decision before dependent dispatch. Inherit effort unless specified.
Keep resolved choices stable
across corrections unless instructed otherwise; record actual selections/fallbacks
in the note, stating when the actual model is unknown. Apply settings through
harness controls, not requests for subagents to change themselves. Role skills
remain model-independent; this mapping does not select the running orchestrator's
model or waive fresh context.

## Isolation and state

Inspect repository instructions, scope, and delivery authorization. Resolve the
requested target branch, otherwise the remote default, and its current base
commit; ask if unresolved. Choose `<id>` as `<short-kebab-slug>-<8-random-hex>`.
Check branch/worktree/note collisions; create `task/<id>` and a sibling
`<repo>-tasks/<id>` worktree from base. Verify path, branch, and HEAD. Never reuse
another task's mutable checkout. Tasks may run concurrently in separate worktrees;
roles within a task run sequentially.

Confirm `.task/<id>.md` is absent at base, then create and commit it. Record
objective, scope, sources, acceptance, base, plan/stage, latest findings/evidence,
decisions/open issues, and all three review records. Replace stale detail while
retaining relevant evidence and accepted references; no transcripts. Files and
note supply context without inherited chat. Use the gate contract's YAML fields
and assessment blocks; retain only latest reviews/current blocker, not a runs array.
Git history preserves repeated executions and prior passes.

## Role protocol

Assignments supply role skill, absolute worktree, branch, objective/scope, exact
input SHA, sources, acceptance, and expected result. Start fresh context (e.g.
`fork_turns="none"`); wait for completion and commit before the next dispatch.
Exclude routine chatter and reasoning transcripts.

Before writing, every role verifies path, branch, empty tracked/untracked status,
and HEAD equal to input SHA. Dirty or mismatched handoffs stop for reconciliation;
preserve changes without reset, deletion, or automatic attribution. Follow
repository instructions and inspect necessary sources.

Only explicit recovery assignments waive clean input. Confirm the interrupted
writer and child processes have stopped; uncertainty prevents another dispatch.
Inspect HEAD, staged/unstaged diffs, and untracked files. Assign the same role in
fresh context using existing fields, current HEAD, and identified changes. It
verifies that inventory, preserves/completes attributable work within its boundary,
commits, and returns cleanly. Uncertain ownership, unexpected changes, or changed
inventory require reconciliation/decision, never reset, deletion, or automatic
attribution. Verify existing commits and recover missing handoffs instead of
duplicating work.

Write boundaries: planner edits affected `spec/` contracts and note using
[specbook](../specbook/SKILL.md); implementer edits authorized implementation/tests
and note; documenter edits documentation, README, documentation examples/assets
and note using [docbook](../docbook/SKILL.md). Reviewers edit note only. Classify
actual purpose/content: skill sources and executable examples can be implementation
regardless of extension/directory. Never silently cross boundaries. Create only
useful task-required spec/docs content; no empty scaffolds or unrelated migrations.

In the note, YAML alone owns workflow stage, review verdicts, and blocker/decision/
recovery status. Do not repeat them as prose readiness, pending/pass, next-action,
or "no issues" claims. Prose holds current findings and verification evidence tied
to input commits; Git retains prior runs.
Freshness is a handoff condition: before committing, every writer reconciles the
whole note with current YAML and verified artifacts, removing superseded claims
while preserving accepted assessment blocks and valid review records. The
orchestrator checks the same consistency alongside the existing gate before
accepting a handoff or dispatching; inconsistent notes return to the writer and
block dependent work.
Update stage/evidence, stage authorized files only, commit with configured signing,
and verify commit/clean status. Even documentation no-change decisions require a
note commit and independent review. Roles never push or open PRs. Return only
`Status`, `Commit`, `Result`, `Evidence`, `Open issues`. Status (`complete`,
`blocked`, `needs-decision`) concerns assignment completion; review verdict
(`pass`, `revise`, `needs-decision`) belongs in Result and the note's YAML record.
Commit prefixes: `plan:`, `review-plan:`, `implement:`,
`review-implementation:`, `document:`, `review-documentation:`.
Set stage to the next action under the gate contract. Reviewers replace their latest
YAML record with verdict, input SHA, and assessed paths while preserving valid other
gates; clear affected downstream records. Keep findings/evidence in the note body.

Retain each review's verdict, exact input SHA separately from its findings commit,
assessed artifacts (plan/specs, implementation/tests, documentation/no-change
rationale), and evidence. Preserve earlier gates when recording later ones.
Review cumulative changes in scope from task base to input SHA, including current
artifacts/dependencies; corrective reviews also recheck prior findings, not just
the latest commit. Notes hold requirements, decisions, findings, and evidence,
not producer reasoning. Reviewers assess requirements/artifacts independently
before comparing author evidence or success claims.

Before tests/runtime operations, identify conflicting shared ports, databases,
containers, accounts, or outputs outside the worktree. Use task-specific resources
where supported; otherwise coordinate exclusive access or serialize conflicts.
Pause conflicting operations if exclusivity is uncertain. Record active constraints
only in the note; worktrees do not isolate external state.

## Gates and corrections

Dispatch planner then plan reviewer at the planner's exact commit. Planning writes
affected contracts and links acceptance/verification to capability paths/rule names.
A plan pass permits implementation; review its exact commit against accepted
plan/specs. After that pass, always dispatch documenter then documentation reviewer
at the documenter's exact commit, including no-change tasks. Reviewer note commits
become next handoff HEADs; accepted artifacts retain their reviewed SHAs.

Passes remain valid on descendants only while assessed artifacts are unchanged.
Compare paths/content to recorded references, including note plan/acceptance.
Documentation/bookkeeping alone can preserve unchanged earlier passes; Markdown
and directories have no blanket exemption. Substantive changes affecting an
assessment invalidate it and downstream gates: record why and rerun affected
author/reviewer sequences. Unrelated changes or advancing HEAD alone do not
invalidate a pass. Retain references and validity decisions in the note.

Blocking findings yield `revise`: return to the responsible author, then fresh
review of its corrective commit. Plan/contract issues return to planner/reviewer
before dependent implementation; code issues to implementer/reviewer; documentation
issues to documenter/reviewer. Documentation roles route discrepancies upstream,
never patch code/contracts or present intended behavior as implemented. After
upstream corrections and passes, rerun documentation and review against corrected
artifacts even if documentation is unchanged. Accounted-for advisories do not block.

Missing material decisions yield `needs-decision`: record the question, ask the
user, and pause dependent work while continuing independent authorized work.
Elapsed time is not approval. If the same blocker survives two corrective attempts
without new evidence, stop, retain attempts/evidence, and report the unresolved issue.

## Delivery

Default to a PR; honor user alternatives and active host authorization rules.
Require all three valid review passes against current artifacts. Fetch/report
the target's current commit and advancement from base. Never automatically merge
or rebase; conflicts/required integration decisions block completion. Integration
changes reopen affected gates and downstream assessments.

Remove `.task/<id>.md` in a `deliver:` commit, preserving role history. Verify clean
status, note absence at base/delivery, zero net diff for its path, and bookkeeping-only
delivery changes. Substantive edits reopen affected gates and downstream stages.
Retain the last note-bearing SHA in delivery evidence; use the checker's archived
state mode after removal. Local gate permission does not prove hosted verification.
Push the explicit branch without force or changing base; create a PR against the
resolved target describing behavior and actual validation. Attach when required.

Inspect hosted mergeability and relevant CI at the exact pushed head. Distinguish
passing, failed, pending, and unavailable checks; no configured checks is not a CI
pass. Failures/conflicts block completion; pending/unknown results mean PR opened,
verification pending. Report current state without indefinite polling or automatic
monitoring. Retain checkout until applicable verification passes and mergeability
is established; report host limitations.

To resume, locate the existing PR/branch and inspect HEAD, status, and checks;
recover the note from committed history if role work is needed. Apply normal gates
to fixes, remove the note again, and push without force. Remove only the clean
worktree after PR creation, required attachment, and resolved verification; retain
branch/history. Failed push, creation, attachment, verification, or dirty cleanup
preserves recoverable checkout/branch. Report only performed checks, distinguishing
simulations/live delivery and PR opened/verification complete.

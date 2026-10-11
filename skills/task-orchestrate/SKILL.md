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
Require fresh-context subagents and Git; report unavailable capabilities without
claiming independent review or isolation.

## Subagent models

Use these built-in preferences; explicit task instructions override them globally
or per role. Unspecified roles retain their preferences.

| Roles | Preferred model |
|---|---|
| task-document, task-review-documentation | GPT-6 Luna (`gpt-6-luna`) |
| task-plan, task-review-plan, task-implement, task-review-implementation | GPT-6.1 Sol (`gpt-6.1-sol`) |

Before dispatch, resolve selections through the harness's advertised model
identifiers and model-selection controls. Use a documented identifier for the
same model; do not guess aliases or equivalent models from another provider.
If a built-in preference is unavailable or selection is unsupported, inherit
the harness default and disclose the fallback. Inherit reasoning effort unless
explicitly instructed. An unsupported explicit model or effort requires a
decision before dependent dispatch; never silently substitute it. Validate
both settings. Keep resolved selections stable across corrective attempts
unless instructed otherwise. Record actual selections and fallbacks compactly
in the task note; if the actual model is unknown, say so. Pass settings through
the harness controls, not as instructions asking a subagent to change itself.
Role skills remain model-independent; this mapping does not select the running
orchestrator's model. Fresh context remains required regardless of fallback.

## Isolation and state

Inspect repository instructions, user scope, and delivery authorization. Resolve
the user's target branch, otherwise the remote default branch, and its current
base commit. Ask if unresolved. Choose `<id>` as `<short-kebab-slug>-<8-random-hex>`.
Check branch, worktree, and note collisions; create branch `task/<id>` and one
worktree in sibling `<repo>-tasks/<id>` from the base. Verify checkout, branch,
and HEAD. Never reuse another task's mutable checkout. Independent tasks may run
concurrently in separate worktrees; roles within a task run sequentially.

Create and commit `.task/<id>.md`, confirming its absence at base. Record objective,
scope, source references, acceptance, base, plan/stage, latest findings/evidence,
decisions/open issues, and three review records. Keep it compact by replacing stale
state, preserving relevant evidence and accepted review references rather than
appending transcripts. Files and note supply context without inherited chat.

## Role protocol

Assignments supply the role skill, absolute worktree, branch, objective/scope,
exact input SHA, source references, acceptance, and expected result. Start a
fresh-context subagent (for example `fork_turns="none"`); wait for its completion
and commit before dispatching the next. Do not send routine chatter or reasoning
transcripts.

Before writing, every role verifies path, branch, empty tracked/untracked status,
and HEAD equal to input SHA. Mismatch or dirty handoff stops for reconciliation;
preserve changes without reset, deletion, or automatic attribution. Follow
repository instructions; inspect sources needed for the assignment.

Write boundaries: planner edits affected `spec/` contracts and note using
[specbook](../specbook/SKILL.md); implementer edits authorized implementation/tests
and note; documenter edits documentation, README, documentation examples/assets
and note using [docbook](../docbook/SKILL.md). Reviewers edit note only. A skill
source or executable example may be implementation regardless of extension or
directory; assess its actual purpose/content. No role silently crosses these
boundaries. Create only useful missing spec/docs content required by the task;
no empty scaffolds or unrelated migrations.

Update stage/evidence, stage only authorized files, commit, preserve configured
signing, verify commit and clean status. Even a documentation no-change decision
must be committed in the note and independently reviewed. Roles never push or
open PRs. Return only `Status`, `Commit`, `Result`, `Evidence`, `Open issues`.
Status (`complete`, `blocked`, `needs-decision`) describes assignment completion;
review verdict (`pass`, `revise`, `needs-decision`) belongs in Result and note.
Commit prefixes: `plan:`, `review-plan:`, `implement:`,
`review-implementation:`, `document:`, `review-documentation:`.

Each review record retains verdict, exact reviewed input SHA (distinct from the
reviewer's later note commit), assessed artifacts, and evidence. Identify the
plan/specs, implementation/tests, or documentation/no-change rationale actually
assessed so later comparisons can establish validity. Preserve earlier records
when writing a later gate; never replace all gates with a single latest verdict.

## Gates and corrections

Dispatch planner then plan reviewer on the planner's exact commit. Planning
writes affected contracts and links acceptance/verification to capability paths
and rule names. A plan pass permits implementation; implementation reviewer
assesses its exact commit against accepted plan/specs. After its pass, always
dispatch documenter then documentation reviewer on the documenter's exact commit,
including no-change tasks. Reviewer note commits become next handoff HEADs;
accepted artifacts remain the recorded reviewed SHAs.

A pass remains valid for descendants only while its assessed artifacts are
unchanged. Compare actual changed paths and content with each recorded reference,
including plan/acceptance changes in the note. Documentation or bookkeeping-only
descendants can preserve an unchanged plan/spec or implementation pass. There is
no blanket Markdown or directory exemption: instruction files can be the product.
Substantive changes affecting an assessment invalidate that gate and downstream
assessments; record why and rerun the affected author/reviewer sequence. Unrelated
changes do not invalidate a pass merely because HEAD advanced. Retain reviewed
references and validity decisions in the note.

Blocking findings yield `revise`: return to the responsible author then fresh
review of the corrective commit. Plan/contract corrections return to planner and
plan reviewer before dependent implementation. Code defects return to implementer
and implementation reviewer. Documentation issues return to documenter and
documentation reviewer. Documenter/reviewer discrepancies route upstream rather
than patching code/contracts or documenting intended behavior as implemented.
After upstream corrections and required passes, rerun documentation and its
review against the corrected artifacts, even if documentation remains unchanged.
Accounted-for advisories do not block a pass.

Missing material decisions yield `needs-decision`: record the question, ask the
user, and continue independent authorized work while dependent work waits. Never
infer approval from elapsed time. If the same blocker survives two corrective
attempts with no new evidence, stop the loop, retain attempts/evidence in the
note, and return the unresolved issue.

## Delivery

Default delivery is a PR; honor user-directed alternatives. Establish required
external-action authorization under active host rules. Require valid passing
plan, implementation, and documentation gates against current assessed artifacts.
Remove `.task/<id>.md` in a `deliver:` commit, preserving all role commits. Verify
clean status, absence of note at base/delivery, zero base-to-delivery net diff for
its path, and bookkeeping-only delivery changes. Substantive edits reopen the
affected gate and downstream stages before delivery.

Push the explicit task branch without force, leaving base branch unchanged; create
a PR against the resolved target describing behavior and actual validation.
Attach it when required. Remove only the clean task worktree after successful PR
creation and required attachment; retain branch/history. Failed push, creation,
attachment, or dirty cleanup retains recoverable checkout/branch and reports the
failure. Distinguish local/disposable simulations from live hosted delivery and
report only checks performed.

---
name: issue-refine
description: Research and clarify a GitHub issue or project draft, split coherent deliveries when needed, and prepare eligible leaf issues for explicit implementation.
---

# Refine an issue

Use `gh`, with `gh api` for capabilities absent from installed commands. Report
missing CLI/authentication/access. Resolve project and repository destinations
from task context and repository conventions; ask if ambiguous. Discover actual
field/option IDs. Keep existing labels, statuses, templates, and scheduling.

Accept an issue URL or project URL/draft item ID. Read the current description,
relevant decisions/comments, parent/children, blocking relationships, active work,
and applicable repository instructions. Do not rewrite work already executing or
delivered without coordination; route material changes to its orchestrator.
Inspect only relevant code, specifications, documentation, and related issues;
research external sources when needed. Keep investigation in agent context.

## Current brief

Rewrite confirmed information into these sections, adapted to existing templates:

- **Outcome:** requested change and why it matters.
- **Scope:** target repositories, included work, and exclusions.
- **Acceptance:** observable completion conditions.
- **Context:** source references, constraints, confirmed decisions, and open
  material questions if any remain.

Separate facts from assumptions. Ask the user for missing material decisions;
use concise issue comments for necessary questions/answers and incorporate
confirmed decisions into the brief. Preserve intent and relevant evidence, not
research transcripts or speculative implementation prescriptions. Do not edit
repository code/specifications/docs, approve a task plan, or launch implementation.

## Placement and splitting

Convert a draft once its destination is known, retaining project membership and
captured intent. Cross-repository parents belong in the planning repository with
the existing `epic` label; implementation children belong in their target repos.
Single-repository work and its parents stay in that repository. Existing misplaced
issues require a placement decision, not an implicit transfer or duplicate.

Split only for independently useful/verifiable deliveries, distinct repositories,
or meaningful dependency boundaries. Each executable child ordinarily delivers
one coherent PR in one repository. Search for existing matching children first;
link/reuse them without silently rewriting unrelated work. A parent owns overall
outcome/scope/completion, not duplicated child descriptions. Never split into task
workflow roles such as plan, test, review, or document.

Use native sub-issues when supported, explicit links otherwise. Record blocking
dependencies separately; a parent relationship alone implies no execution order.
Include parent and actionable children in the project as needed. Keep parents
in `Backlog` during refinement; never enqueue them alongside their children.

## Readiness and return

Only open executable leaves with a resolved target, clear scope/acceptance,
confirmed material decisions, and satisfied blocking dependencies become `Ready`.
Readiness permits planning; it is not specification/implementation approval.
Unresolved or blocked work stays `Backlog`, with a concise explanation. Preserve
priority, dates, estimates, and assignees unless changes are explicitly requested.

Before replacing descriptions, reread bodies/decisions and reconcile intervening
edits. Recheck relationships/dependencies before setting Ready. Verify each body,
conversion/link, membership, and status; inspect partial results before retrying
so issues and links are not duplicated. A failed update is not claimed successful.

Return concise Ready issue URLs, parent/child/dependency links, and remaining
questions or partial failures. Return the URL for explicit `task-orchestrate`
invocation; do not dispatch agents, select the next issue, or load its lifecycle.

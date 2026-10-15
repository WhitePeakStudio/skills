---
name: issue-create
description: Capture a request as a GitHub issue or project draft, respecting repository ownership and backlog conventions without duplicating existing work.
---

# Capture an issue

Use `gh`; report missing CLI, authentication, or required issue/project access.
Use `gh api` when installed commands lack a capability. Resolve project, target
repositories, and planning repository from explicit instructions and repository
conventions; ask when ambiguous. Discover field/option IDs, never hardcode them.
Read only relevant conventions/templates and existing issues/project items.

Search for matching work before creating, including closed issues when relevant.
Return a clear duplicate's URL/item ID without editing it; uncertain matches need
clarification, not automatic consolidation.

Follow existing placement conventions: early ideas without a known destination
are project drafts; cross-repository initiatives belong in the planning repository
with its existing `epic` label; single-repository work belongs in that repository.
If required conventions, labels, or statuses are absent, report rather than invent
them. Do not transfer issues or change repository/project configuration.

Capture the requested outcome, known scope/exclusions, constraints, and open
questions using the existing template when available. Preserve intent without
inventing acceptance, product decisions, or implementation plans. Add the item
to the selected project as `Backlog`. Preserve supplied priority/scheduling;
do not guess priorities, estimates, deadlines, or assignees.

For an issue, set exactly one existing workflow label when intent is clear:
workflow:task for repository changes; workflow:agent for standalone actions or
research. Ask when ambiguous or required labels are missing. Drafts retain the
intended route in their captured scope until conversion. Do not alter active work.

Use body files/stdin for multiline text. If updating a captured description is
explicitly authorized, reread it and reconcile intervening edits before replacing.
Verify creation, membership, and status separately. On partial/unknown failure,
inspect actual issues/items before retrying; retain created URLs and repair only
the missing authorized operation. Never blindly repeat creation.

Return the issue URL or project URL/draft item ID, placement, verified status,
and unresolved questions/partial failures. Keep research for refinement; do not
mark `Ready`, launch execution, or load task workflow instructions.

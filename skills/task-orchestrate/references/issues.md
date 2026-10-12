# Issue input and delivery

Read only for an explicitly supplied issue URL. Use `gh` and, where needed,
`gh api`; report missing CLI/authentication/issue or project access. Resolve the
project and target repository from task context/conventions; ask if ambiguous.
Discover status field/option IDs instead of guessing or creating configuration.
Do not pick the next Ready issue, refine the backlog, or load intake skills.

## Start or resume

Fetch the current brief, relevant decisions, relationships/dependencies, project
status, execution comments, and linked PRs. Distinguish a new task from recorded
execution before checking new-start eligibility. Reuse an existing task/PR for
resume; never create a second checkout because its status is no longer Ready.
If a writer may still be active, confirm it stopped before recovery/dispatch.
Unknown execution ownership blocks another run.

A new start requires an open executable leaf in `Ready`, one resolved target
repository, satisfied blocking dependencies, and no active execution or delivered
PR. Reject parents/epics, drafts, non-Ready issues, unresolved material decisions,
or existing work; report the reason rather than bypassing refinement. V1 assumes
one dispatcher; project status/assignment is not a distributed atomic lock.

Create the normal isolated task worktree/note. Keep the issue URL as a source and
record its fetched revision (`updatedAt`) once in bookkeeping; capture the agreed
requirements in the existing task contract, without comments/research transcripts.
The planner still owns authoritative specifications and the implementation plan;
all three independent reviews and the existing state schema remain unchanged.

Before role dispatch, record task ID, target repository, branch, absolute worktree,
and base SHA in one concise issue execution comment; move the item to `In progress`
and verify both writes. On partial failure, preserve the checkout/created comment
and repair missing association/status rather than create another task or comment.
Record/reuse the known comment on resume. Do not invent assignees or field values.

Keep project status `In progress` through internal review/correction loops. Report
material blockers/questions concisely on the issue without another status. Before
resuming and delivery, compare current issue requirements/confirmed decisions with
the accepted contract. Material changes use the normal planning/review route;
metadata/comments alone do not invalidate gates. Never silently adopt changed
scope or overwrite the user's description. A reopened contract can also require
fresh implementation and documentation assessments under existing rules.

## Delivery and completion

Follow [delivery](delivery.md). On PR creation, explicitly link the issue and PR,
update the execution comment with the PR URL, and move the item to `In review`.
Verify the updates; report actual hosted verification, including failures/pending
checks. Failed issue/project updates preserve the PR, branch, and recoverable
checkout until reconciled; retry only missing operations. Opening a PR never
closes the issue or sets `Done`.

On explicit follow-up, inspect the existing PR/outcome, even if the issue was
automatically closed after merge. Only an observed merge or explicit user
acceptance permits `Done` and completed issue closure. Closed-unmerged PRs or
abandoned issues are not completed deliveries. Reconcile status/closure separately
and verify results. Do not merge, monitor, poll indefinitely, or close a parent
merely because its child count is complete; parent outcome assessment is separate.

Issue briefs own requested outcomes; specifications own required behavior; the
task note owns execution state; project status describes coarse delivery progress;
Git preserves role history. Roles do not manage GitHub issues or project status.

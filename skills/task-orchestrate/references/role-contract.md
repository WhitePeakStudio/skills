# Shared role contract

Load this contract, [note state](state.md), your assigned role skill, and relevant
repository artifacts once per assignment. Lifecycle/models/delivery belong to the orchestrator;
load [recovery](recovery.md) only for an explicit recovery assignment. Routine
investigation and reasoning stay in subagent context, not assignments or notes.

Assignments contain only `Worktree and branch`, `Objective and scope`,
`Input commit and relevant sources` (including role skill), and
`Acceptance and expected result`. Use references instead of repeating contracts.
Start each assignment fresh; no producer conversation accompanies review.

Before writing, verify absolute path, branch, exact input HEAD, and empty
tracked/untracked status. Follow repository instructions and necessary sources.
Mismatch/dirty input stops normal work: preserve changes without reset, deletion,
or automatic attribution. Only explicit recovery waives clean input.

Write only your role's authorized files and note; reviewers write note only and
never fix reviewed artifacts. Classify content, not extension/directory: skill
sources and executable examples may be implementation. Create only useful
task-required spec/docs content, without empty scaffolds or unrelated migrations.
Before runtime checks identify shared ports, databases, containers, accounts, or
external outputs; isolate them or coordinate exclusive/serial access. Uncertain
exclusivity pauses conflicting operations. Keep only active constraints in the note.

## Assessment and correction

Review cumulative scope from task base to assigned input, rechecking earlier
findings on corrections. Assess requirements/artifacts independently before
comparing producer evidence. Keep receipt input separate from findings commit;
[state](state.md) defines provenance, artifact selection and approval validity.
Preserve unchanged approvals, invalidate affected gates and downstream records
when assessed content changes; Markdown/bookkeeping has no blanket exemption.

Author handoff stages: `plan` -> `review-plan`, `implement` ->
`review-implementation`, `document` -> `review-documentation`. Reviewer passes
route respectively to `implement`, `document`, `deliver` with valid prerequisites.
Incomplete authors remain at their author stage. Blocking findings yield `revise`: return to the responsible
author then fresh review. Contract/scope issues return to plan; code to implement;
docs to `document`. Stale prerequisites restore the affected author/review gate.
Code/contract corrections require fresh downstream documentation and review.
Other outcomes block for reconciliation; the orchestrator owns [full transitions](gates.md#transitions).
Accounted-for advisories do not block; retain dispositions still relevant to scope.

Missing material decisions yield `needs-decision`: record the question, ask the
user, pause dependent work, continue only independent authorized work. Time is
not approval. Stop when the same blocker survives two corrective attempts without
new evidence; retain its count and concise evidence rather than renaming/resetting.

## Handoff

YAML alone owns workflow stage, review verdicts, and blocker/decision/recovery
status. Prose contains current findings and concise verification evidence tied
to input commits, never readiness, next-action, pending/pass or "no issues" summaries.
Before committing, refresh the whole note against YAML and verified artifacts;
remove superseded claims while preserving marker-bounded assessment text/YAML records.
The orchestrator checks the same consistency with the existing gate before
accepting/dispatching. Inconsistent notes return to their writer and block dependent work.

Freshness-only repair continues the same assignment. Authors use their role prefix;
reviewers use note-only `task:` commits preserving assessment blocks/records, so
the original findings commit remains attached to its input. Substantive corrections
use normal author/review loops. Do not manufacture review passes for your own work.

Set the next stage/records, stage authorized paths only, commit with configured
signing and your role prefix, then verify commit and clean status. Even no-change
documentation requires its own assessment commit and independent review.
Roles never push or open PRs.

Return only `Status: complete | blocked | needs-decision`, `Commit`, `Result`,
`Evidence`, `Open issues`. Status concerns assignment completion, not acceptance;
review verdict belongs in Result and note YAML. Keep fields concise; cite commits,
paths and checks. Expand detail only for an actionable finding, decision or limitation.

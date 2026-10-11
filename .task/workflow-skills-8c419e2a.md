# workflow-skills-8c419e2a

## Objective and scope

Add five compact, separate instruction skills: `task-orchestrate`, `task-plan`,
`task-review-plan`, `task-implement`, and `task-review-implementation`. Support
fresh-context role subagents, mandatory plan/review and implementation/review
loops, and a default pull-request delivery. Update README and plugin presentation
to Repository Skills, version 0.2.0. Preserve package identity, marketplace, and
existing specbook/docbook byte for byte. No helper scripts, reusable templates,
extra reports, or orchestration service.

## Inputs

- Worktree: `C:/Users/jimiv/Documents/Codex/2026-10-11/in/work/skills-tasks/workflow-skills-8c419e2a`.
- Branch: `task/workflow-skills-8c419e2a`.
- Input commit: `fbc226fd4532fa7ca85c75d8b24e4df59a9ac86d`.
- Sources: task assignment, README.md, plugin.json, .agents/plugins/marketplace.json,
  skills/specbook/SKILL.md, skills/docbook/SKILL.md.

## Acceptance

- Exactly five new skill directories have SKILL.md with valid `name` and
  `description` frontmatter; names match folders. Relative links resolve.
- Orchestrator uses one task worktree/branch and one `.task/<id>.md` note;
  `<id>` is `<short-kebab-slug>-<8-random-hex>`, branch `task/<id>`, and worktree
  is in sibling `<repo>-tasks/<id>`. Check collisions and creation results.
- Independent tasks may run concurrently in isolated worktrees. Within a task,
  fresh-context roles run sequentially; each finishes and commits before the
  next receives its assignment. Never share another task's mutable checkout.
- Each role verifies assigned path, branch, clean state, and input commit before
  writing. Dirty or mismatched handoffs stop for reconciliation without reset,
  deletion, or automatic attribution to unrelated changes.
- Assignments carry worktree/branch, objective/scope, exact input commit/sources,
  and acceptance/expected result. Returns carry Status, Commit, Result, Evidence,
  Open issues. The task note holds current objective, scope, acceptance, plan,
  stage, latest findings/evidence, and decisions; replace stale state rather than
  accumulating logs. References supply context without inherited chat history.
- Plan reviewer evaluates the exact planner commit; implementation reviewer
  evaluates the exact implementation commit. Record reviewed input separately
  from each review's own note commit. Acceptance never applies implicitly to a
  later commit; corrections receive a fresh review of their exact commit.
- Plan corrections return to planner then plan reviewer. Implementation
  corrections return to implementer then implementation reviewer; a scope or
  plan change goes through the plan/review gate again before implementation.
- Missing material decisions are recorded and requested from the user; roles
  perform independent authorized work while waiting, without inventing approval.
  Stop when the same blocker survives two corrective attempts with no new
  evidence; record attempts/evidence and return the unresolved issue.
- Default delivery removes `.task/<id>.md` in a delivery commit, preserves all
  role commits, confirms clean state and zero task-note net diff, pushes without
  force, and creates a PR. Remove a clean task worktree only after successful PR
  creation and required attachment; retain branch/history. Failed push/PR or
  dirty cleanup retains the worktree and reports recoverable state. Alternate
  delivery requires the user's instruction. No push/PR by role subagents; orchestrator delivers.
- README introduces all seven skills, role order, correction loops, concurrent
  task isolation, compact handoffs, task-note lifecycle, and default delivery.
  Manifest version is 0.2.0 and displayName Repository Skills. Preserve manifest
  name `skills`, repository/author identity, and marketplace catalog identity.
- Validate frontmatter, local links, JSON/metadata consistency, preserved files,
  and disposable-repository lifecycle scenarios listed below. Report actual
  evidence and distinguish simulations from a live hosted PR.

## Plan

1. Put the lifecycle contract and cross-skill links in task-orchestrate. Keep
   each role skill narrowly scoped, specifying its entry checks, role duties,
   note update/commit, and compact return. Use explicit fresh-context spawning
   and bounded corrections; avoid duplicating the full orchestrator protocol.
2. Planner writes/revises only the task note. Plan reviewer checks feasibility,
   scope, acceptance, risks, decisions and correction handling, then commits its
   findings in that note. Implementer changes authorized files, verifies them,
   updates the note and commits. Implementation reviewer reads the assigned
   commit/diff, checks acceptance and evidence, records actionable findings in
   the note and commits; it does not silently fix the implementation.
3. Update README and plugin metadata for the enlarged instructions-only package.
   Keep the existing marketplace entry intact. Do not modify specbook/docbook.
4. Validate files and exercise the described git protocol in disposable repos
   outside the deliverable tree. Use temporary commands/tool stubs when remote
   delivery cannot be performed; save no helper artifacts in the package.
5. Commit implementation and its evidence, run a fresh implementation review,
   correct/review as necessary, and return the final local commit. The outer
   orchestrator handles delivery authorization and final task-note cleanup.

## Validation scenarios

- Success: sequential planner/reviewer/implementer/reviewer commits, then delivery
  deletion; role history survives and base-to-delivery diff has no `.task` file.
- Corrections: rejected plan and implementation each receive corrective commits
  and new review; implementation waits for the current accepted plan.
- Concurrency: two unique task IDs create separate sibling worktrees and branches;
  changes and task notes do not leak across checkouts.
- Attribution: reviewers record the supplied planner/implementation SHA, not
  their own later review commit; later corrections require new approval.
- Dirty handoff: pending tracked/untracked changes cause a halt and remain intact.
- Stalled progress: the same blocker after two corrective attempts without new
  evidence ends the loop with the blocker and evidence preserved.
- Missing decision: record the question and pause dependent work without treating
  elapsed time as an answer.
- Failed delivery: simulated failed push or PR preserves checkout/branch/note or
  note history and permits a retry without force push or premature cleanup.
- Successful delivery: simulate push/PR success, verify task-note net diff zero,
  remove only a clean worktree, and retain branch and role commits. Label the
  hosted portion as simulated when no real PR is created.

## Stage

Plan accepted. Ready for implementation against the accepted plan below; no
implementation or delivery performed. Plan-review input commit:
`9d634387d6c57d72cef78604230431a5e9fe7891`. The review commit is a later note-only
commit and is not the reviewed input.

## Latest findings and evidence

- Verdict: accepted. The five separate instruction skills fit the existing
  instructions-only package and `skills/` discovery layout. The plan assigns
  narrow role duties and centralizes lifecycle rules in task-orchestrate;
  no new runtime, helper scripts, or auxiliary product files are needed.
- Scope and acceptance are complete: exact skill names, compact handoffs,
  fresh-context sequential roles, concurrent task isolation, immutable review
  attribution, correction gates, missing decisions, bounded stalled progress,
  role commits, and recoverable default PR delivery all have explicit coverage.
- Disposable git scenarios make the lifecycle verifiable without a live hosted
  PR. They cover success, both correction loops, concurrency, review attribution,
  dirty handoffs, stalled progress, missing decisions, failed delivery, and clean
  cleanup. Record command/results and distinguish simulated remote actions from
  actual hosted delivery in the implementation evidence.
- During implementation, make the entry-check contract and review outcomes
  explicit in each role skill; relative cross-links can carry shared lifecycle
  details. Delivery must validate that the task-note path was absent at the base
  and is absent at delivery, preserving all role commits and a zero net diff.
  These clarify existing acceptance rather than add scope or a decision gate.
- Inspected README.md, plugin.json, .agents/plugins/marketplace.json, and both
  existing SKILL.md files. Current manifest is 0.1.0 with Specbook & Docbook
  presentation; package identity is `skills` and marketplace source is `./`.
  Updating presentation/version while preserving catalog and existing skills
  byte for byte is feasible and can be checked by git diff or file hashes.
- Assigned absolute checkout and branch were verified. Before this review's
  write, status was clean and HEAD exactly matched the reviewed input SHA above.
  No `.codegraph/` exists. Git uses a command-local safe.directory override.

## Decisions and open issues

- No outstanding material decision or blocking plan finding.
- Preserve marketplace catalog content and existing specbook/docbook. Workflow
  definitions belong in the five new SKILL.md files; this task note is temporary.
- Role subagents perform no push/PR actions. The root orchestrator is authorized
  to deliver the implementation through push/PR and final task-note cleanup.

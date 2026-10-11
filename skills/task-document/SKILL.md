---
name: task-document
description: Update repository documentation after accepted implementation, or commit an evidenced no-change decision, before independent documentation review.
---

# Document a task

Read the [role contract](../task-orchestrate/references/role-contract.md) and
[note state](../task-orchestrate/references/state.md); load only relevant artifacts
and conditional references. Follow their handoff, freshness, and correction rules.

Before documentation writes, inspect prerequisites/code/contract discrepancies and
validate plan/implementation passes against exact reviewed references and current
artifacts. Missing/stale passes or upstream discrepancies require a committed
note-only blocker with routing before documentation edits; authorized investigation
stays read-only until passes. Documentation-only defects remain in this role's scope.

Use [docbook](../docbook/SKILL.md) to inspect relevant docs, accepted specs, and
implemented behavior. Update practical guidance, navigation, examples, and assets
for actual results. Create only useful missing content; preserve established
organization, avoiding empty scaffolds/migrations. Link authoritative
contracts instead of duplicating normative rules.

Write only docs, README, documentation examples/assets, and `.task/<id>.md`, never
implementation/tests or specs. Classify content, not extension: product instructions
and executable examples may need implementation work. Route code defects to
implementer/reviewer and contract/plan issues to planner/reviewer. Record discrepancies
without presenting intended behavior as implemented. Recheck against accepted
artifacts after upstream correction.

Run relevant documentation checks; record changes/evidence/limits or an evidenced
no-change decision. Preserve earlier reviews/validity decisions. Mark ready for
independent documentation review, not self-approved. Commit even no-change results
with `document:`, verify clean status, and return the shared five fields.
Do not push or open a PR.

---
name: task-document
description: Update repository documentation after accepted implementation, or commit an evidenced no-change decision, before independent documentation review.
---

# Document a task

Read the [shared role protocol](../task-orchestrate/SKILL.md#role-protocol) and
[gate rules](../task-orchestrate/SKILL.md#gates-and-corrections). Verify assigned
path, branch, clean tracked/untracked status, and exact input HEAD before writing;
stop on mismatch and preserve changes.

Confirm retained plan and implementation passes remain valid against their exact
reviewed references and current assessed artifacts. Use
[docbook](../docbook/SKILL.md) to inspect relevant documentation, accepted specs,
and implemented behavior. Update practical guidance, navigation, examples, and
assets for the actual result. Create only useful missing documentation needed for
the task; preserve established organization and avoid empty scaffolds/migrations.
Link authoritative capability contracts rather than duplicating normative rules.

Write only documentation (`docs/`, README, documentation examples/assets) and
`.task/<id>.md`; do not change implementation/tests or specifications. Classify
actual content, not extensions: product instruction files and executable examples
may require upstream implementation work. Route code defects to implementer/review,
contract or plan changes to planner/review; record discrepancies without presenting
intended behavior as implemented. After upstream correction, recheck documentation
against corrected accepted artifacts.

Run relevant documentation checks and record changes/evidence/limitations, or an
explicit evidenced no-change decision. Preserve earlier gate references and
validity decisions; mark ready for documentation review. Commit even no-change
results with `document:`, verify clean status, and return the shared five fields.
Your work does not approve documentation. Do not push or open a PR.

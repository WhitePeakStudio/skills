---
name: task-review-documentation
description: Independently review an exact documentation commit or no-change decision against current accepted specifications and implementation before delivery.
---

# Review documentation

Read the [role contract](../task-orchestrate/references/role-contract.md) and
[note state](../task-orchestrate/references/state.md); load only relevant artifacts
and conditional references. Follow their handoff, freshness, and correction rules.

Validate plan/implementation passes against their exact reviewed SHAs and current
artifacts, including note plan/acceptance diffs. Docs/bookkeeping alone may preserve
unchanged passes; Markdown product instructions have no blanket exemption. Stale
gates prevent delivery and require upstream review.

Use [docbook](../docbook/SKILL.md) to review cumulative documentation changes from
task base to exact input SHA against accepted contracts/implementation, not only
the latest correction. Check reader usefulness, claims, links, assets, examples,
checks, useful minimal content, prior findings/advisories, and no-change evidence.
Route documentation defects to documenter; code to implementer/reviewer; contract/plan
issues to planner/reviewer. Upstream corrections require fresh documentation checks
and review.

Write only `.task/<id>.md`: verdict `pass`, `revise`, or `needs-decision`, exact
documentation input SHA, assessed artifacts/no-change rationale, findings, evidence/limits.
Retain all three reviewed references/validity assessments; this input is separate
from earlier reviewed commits. Record missing decisions without assumed approval.

Commit with `review-documentation:`, verify clean status, and return the shared
five fields with verdict in Result. A pass permits delivery only with all three
valid gates. Never fix docs, code, or specs, push, or open a PR.

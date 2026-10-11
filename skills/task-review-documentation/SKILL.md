---
name: task-review-documentation
description: Independently review an exact documentation commit or no-change decision against current accepted specifications and implementation before delivery.
---

# Review documentation

Read the [shared role protocol](../task-orchestrate/SKILL.md#role-protocol) and
[gate rules](../task-orchestrate/SKILL.md#gates-and-corrections). Verify assigned
path, branch, clean tracked/untracked status, and exact input HEAD before writing;
stop on mismatch, preserving changes. Only an explicit recovery assignment may
use the shared interrupted-role exception to the clean-input check.

Validate retained plan and implementation passes by comparing their exact reviewed
SHAs and assessed artifacts with current content; inspect actual diffs, including
plan/acceptance note changes. Documentation/bookkeeping descendants may preserve
unchanged earlier passes; Markdown product instructions have no blanket exemption.
A stale earlier gate prevents delivery and requires the appropriate upstream review.

Use [docbook](../docbook/SKILL.md) to review documentation at this exact input
against accepted contracts and implemented behavior. Check reader usefulness,
claims, links, assets, examples, relevant checks, and required minimal content for
missing structures. Independently assess an evidenced no-change decision. Check
prior findings/advisory dispositions. Route documentation defects to documenter;
code defects to implementer/reviewer; contract/plan changes to planner/reviewer.
Upstream correction requires fresh documentation checks and review.

Review cumulative changes in your scope from the recorded task base to this
input SHA under the shared review rules, not just the latest corrective commit.

Write only `.task/<id>.md`: record verdict `pass`, `revise`, or `needs-decision`,
exact documentation input SHA, assessed artifacts/no-change rationale, findings,
and evidence/limitations. Retain all three reviewed references and validity
assessments; this review's input is independent of earlier reviewed commits.
Record missing material decisions without assuming approval.

Commit with `review-documentation:`, verify clean status, and return the shared
five fields; Result carries the verdict. A pass permits delivery only when all
three gates remain valid. Do not fix documentation, code, or specs, push, or open a PR.

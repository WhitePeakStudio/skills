---
name: task-review-plan
description: Independently review an exact plan and specification commit for contract quality, feasibility, acceptance coverage, scope, and unresolved decisions.
---

# Review a plan

Read the [shared role protocol](../task-orchestrate/SKILL.md#role-protocol) and
[gate rules](../task-orchestrate/SKILL.md#gates-and-corrections). Verify assigned
path, branch, clean tracked/untracked status, and exact input HEAD before writing;
stop on mismatch, preserving changes.

Review that input's plan and affected contracts using
[specbook](../specbook/SKILL.md). Check authoritative capability boundaries,
required sections/index, named rule acceptance coverage, consistency with related
contracts, and useful minimal creation when structures were missing. Check task
acceptance and verification links to capability paths/rule names, or the evidence
for a no-contract-change decision. Assess feasibility, scope, repository
constraints, risks, and material decisions. Check prior findings and advisory
dispositions. Do not rewrite contracts/plan or silently expand scope.

Write only `.task/<id>.md`: record verdict `pass`, `revise`, or `needs-decision`,
exact reviewed input SHA, assessed plan/specification artifacts, actionable
findings, and evidence/limitations. Preserve current plan, relevant decisions,
and other gate references; invalidate affected downstream assessments when
necessary. Blocking findings require correction and fresh review; accounted-for
advisories do not block a pass. Record missing material decisions without assumed
approval.

Commit with `review-plan:`, verify clean status, and return the shared five fields;
Result carries the verdict. Assignment completion is separate from acceptance.
Your note commit is distinct from reviewed input; descendants retain a pass only
under shared artifact-validity rules. Do not implement, document, push, or open a PR.

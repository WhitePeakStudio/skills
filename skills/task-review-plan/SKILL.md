---
name: task-review-plan
description: Independently review an exact plan and specification commit for contract quality, feasibility, acceptance coverage, scope, and unresolved decisions.
---

# Review a plan

Read the [role contract](../task-orchestrate/references/role-contract.md) and
[note state](../task-orchestrate/references/state.md); load only relevant artifacts
and conditional references. Follow their handoff, freshness, and correction rules.

Use [specbook](../specbook/SKILL.md) to review the exact input plan/contracts. Check
capability boundaries, required sections/index, named-rule acceptance coverage,
related-contract consistency, and useful minimal creation. Check capability/rule
links for task acceptance/verification or evidenced no-contract-change decisions.
Assess feasibility, scope, constraints, risks, decisions, prior findings, and advisory
dispositions. Do not rewrite plan/contracts or silently expand scope.

Review cumulative changes in scope from task base to input SHA, not only the latest
correction. Write only `.task/<id>.md`: verdict `pass`, `revise`, or `needs-decision`,
exact reviewed SHA, assessed plan/spec artifacts, actionable findings, evidence/limits.
Preserve plan, relevant decisions, and other reviews; invalidate affected downstream
gates. Blockers require correction/fresh review; accounted-for advisories do not block.
Record missing decisions without assuming approval.

Commit with `review-plan:`, verify clean status, and return the shared five fields
with verdict in Result. Completion differs from acceptance; your note commit
differs from reviewed input. Descendant passes follow shared validity rules.
Do not implement, document, push, or open a PR.

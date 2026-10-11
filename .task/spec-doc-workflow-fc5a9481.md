# Specification and documentation workflow

## Objective and scope

Implement the user-approved evolution of the compact task workflow. Base:
`e9e7ae1f8f4f0c9703408c9a4525288c46695f2b` (PR #1 merged into main).
Branch: `task/spec-doc-workflow-fc5a9481`.
Add task-document and task-review-documentation; update five task skills,
README and plugin metadata. Preserve specbook, docbook and marketplace bytes.
No helper scripts, templates, reports, service or package scaffolding.

## Acceptance

- Planning writes affected specifications using specbook and the task note;
  plan review checks contract changes. Acceptance links to capability/rule names.
- Implementation writes authorized implementation/tests and note; no contract
  edits or documentation work reserved for the later gate.
- Documentation and independent review run after implementation review on every
  task, including committed/reviewed no-change decisions, using docbook.
- Documenter writes documentation/README/examples/assets and note only; all
  reviewers write note only. Scope/code/contract defects route upstream.
- One worktree/branch/note, fresh-context sequential roles, exact input SHA
  checks, compact handoffs and role commits remain. Add document: and
  review-documentation: prefixes; retain all three accepted review references.
- Earlier passes remain valid only when assessed artifacts are unchanged;
  relevant changes invalidate the affected gate and downstream assessments.
  Task bookkeeping alone does not invalidate passes.
- Missing spec/docs structures get only needed useful content; no empty scaffold
  or unrelated migrations. Both specialist skills retain existing rules.
- Existing stalled-progress, decision, dirty-handoff, concurrency, failed-delivery
  and cleanup behavior remains; delivery waits for all three review gates.
- Nine skills validate; README requires all seven task skills plus specbook and
  docbook together; version 0.3.0, display Repository Skills, identities preserved.

## Plan

1. Independent plan review checks this user-approved design and boundaries.
2. Implementer updates seven task skill entrypoints and plugin metadata. Treat
   SKILL.md files as product instructions. Existing specialist files/catalog stay
   untouched; no new product spec is needed to duplicate the supplied contract.
3. Independently review implementation; correct and re-review concrete findings.
4. Documenter updates package README only after implementation review, using
   docbook. Documentation reviewer checks it against the accepted implementation.
5. Root removes this note in deliver: commit, verifies net diff, pushes and opens
   a PR against main; attach PR then remove only the clean task worktree.

## Verification

Validate nine frontmatters, prose links/anchors, metadata, directories, preserved
bytes, whitespace and actual role write boundaries. Disposable repositories and
fresh-context subagents exercise specification planning/review corrections,
implementation against acceptance, documentation timing/corrections/no-change,
upstream discrepancy routing, minimal missing structures and gate invalidation.
Re-run existing Git lifecycle fixture for concurrency, dirty cleanup, failed push,
history and task-bookkeeping preservation. Fixture hosted delivery is simulated;
actual PR publication is checked separately.

## Stage and accepted reviews

Plan review: pass. Reviewed input: `87320f51efbe996cf396b17a6179fd0c1e7ed2ac`.
Plan assessed artifacts: objective/scope, acceptance, plan and verification in this note; supplied contract and existing package boundaries. These remain unchanged.
Implementation review: pass. Reviewed input: `47bb45808da207cd855346e4c89c8fc259436af8`.
Implementation assessed artifacts: the seven task skill entrypoints and plugin.json;
accepted plan/scope/acceptance/verification remain unchanged against the plan input.
Ready for mandatory documentation and independent documentation review; that gate
is pending, including the README dependency/installation update.

## Latest findings, evidence and decisions

PR #1 merged; current base contains version 0.2.0 and five workflow skills.
No .codegraph exists. Use command-local safe.directory; preserve signed commits
(signing requires escalated execution on this Windows host).
Both doc stages always run; create minimal missing structures as needed.
No unresolved user decision. Role subagents do not publish; root is authorized.

## Plan review findings and evidence

Verdict: **pass** for input `87320f51efbe996cf396b17a6179fd0c1e7ed2ac`.
No blocking findings or missing material decisions.

Read all five current task skills, specbook, docbook, README, plugin.json and
marketplace metadata. Exact assigned path/branch/HEAD and clean tracked/untracked
status verified. Scope is feasible as instruction-only changes: seven task skills,
nine total skill frontmatters, metadata version 0.3.0 and subsequent README update.
Acceptance defines each role's write boundary, mandatory documentation/no-change
review, three retained reviewed SHAs, artifact-based gate invalidation and upstream
correction routing. Existing failure, decision and cleanup controls remain explicit.

Advisory disposition: the approved package-specific choice to avoid duplicating
this supplied contract in a new product spec, and to update README only, is scoped
to this repository change. It must not become a general exemption from specbook,
docbook, useful missing structures or their rules in the evolved task skills.
Verification must exercise those general rules in disposable task repositories.
Fixture delivery remains simulated; live delivery evidence belongs to root.
## Implementation evidence

Updated seven task skill entrypoints and plugin metadata to 0.3.0. Shared protocol
owns role boundaries, retained artifact-based review validity, upstream routing,
mandatory documentation/no-change review and three-gate delivery. README deferred
to documenter; specialist skills and marketplace unchanged. No new package files
beyond the two requested SKILL.md entrypoints.

Package validator passed: nine skill frontmatters, 31 local links/anchors,
metadata identity/version and preserved specialist/catalog bytes; diff --check
passed. Existing Git lifecycle fixture has ten passes at external
work/workflow-check-eab0132f/verification.json (local simulated delivery).
Fresh-context behavior fixtures and live hosted delivery belong to subsequent
roles/root; no behavioral or live publication result claimed here.
No open implementation decision. Input: e1ddd4acc9d2f19c26ae32ae8337c1b7e4b32a83.

## Implementation review findings and evidence

Verdict: **pass** for exact input
`47bb45808da207cd855346e4c89c8fc259436af8`; no blocking findings or missing material
decisions. Reviewed against base `e9e7ae1f8f4f0c9703408c9a4525288c46695f2b` and
accepted plan input `87320f51efbe996cf396b17a6179fd0c1e7ed2ac`. Objective/scope,
acceptance, plan and verification sections are unchanged, so the plan pass remains
valid. Assigned absolute path, branch, exact HEAD and empty tracked/untracked
status were verified before writing.

Assessed files: `skills/task-orchestrate/SKILL.md`, `skills/task-plan/SKILL.md`,
`skills/task-review-plan/SKILL.md`, `skills/task-implement/SKILL.md`,
`skills/task-review-implementation/SKILL.md`, `skills/task-document/SKILL.md`,
`skills/task-review-documentation/SKILL.md`, and `plugin.json`. Read unchanged
specbook/docbook and README as dependency/boundary context.

Concrete evidence: planner uses specbook for affected capability contracts and
named-rule acceptance/verification; plan reviewer assesses those contracts or
the evidenced no-contract-change decision. Implementation reserves spec/docs work
for their authors. Shared protocol classifies sources by actual purpose, keeps
reviewers note-only, preserves all three exact assessed references, and invalidates
affected gates on substantive artifact changes rather than HEAD advancement.
Documenter and documentation reviewer use docbook, assess actual accepted behavior,
route contract/code discrepancies upstream, and require fresh documentation checks
after correction. Every task commits and independently reviews even an evidenced
documentation no-change decision. Delivery requires all three valid passes.
Fresh-context sequential roles, dirty-handoff preservation, decision/stalled-loop
controls, isolated worktrees and recoverable failed delivery remain explicit.

Independent absolute-path run of `work/validate_package.py <worktree> 0.3.0`
passed: nine frontmatters, 31 local links/anchors, preserved specialist/catalog
bytes, metadata identity and 0.3.0 version. Base-to-input `git diff --check` passed.
Read `work/workflow-check-eab0132f/verification.json`: ten Git lifecycle passes;
it explicitly limits delivery to local simulation and excludes agent decisions.

Accounted-for advisory: README is deliberately unchanged until the next authorized
role. Its five-task-skill standalone installation guidance must become seven task
skills plus specbook/docbook together, preserving sibling layout because direct
relative links now require those specialist dependencies. This is the accepted
documentation-stage requirement, not a product-source blocker. The approved
package-specific no-new-spec/README-only decisions have not become general
exemptions in the role sources.

Limits: behavioral fixtures remain root-owned and in progress; this review records
source inspection and static/Git evidence, not fresh behavioral fixture execution
or live hosted publication. Documentation gate remains pending; delivery is not
approved by this pass.

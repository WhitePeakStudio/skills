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

Plan ready for independent review. No implementation yet.

## Latest findings, evidence and decisions

PR #1 merged; current base contains version 0.2.0 and five workflow skills.
No .codegraph exists. Use command-local safe.directory; preserve signed commits
(signing requires escalated execution on this Windows host).
Both doc stages always run; create minimal missing structures as needed.
No unresolved user decision. Role subagents do not publish; root is authorized.

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
Implementation review: pass for exact input
`05a0fe89defb8bcee8f1b90404051cddc6ec1716`; current assessed artifacts are the
seven task skill entrypoints and plugin.json. Prior reviewed input
`47bb45808da207cd855346e4c89c8fc259436af8` remains retained as historical evidence;
its pass was invalidated by the task-document instruction correction. The fresh
pass assesses that correction and all implementation acceptance against the
unchanged accepted plan/scope/acceptance/verification.
Prior documentation completed at `5f37323a45d958fabf6fa9411328090dc978cb53`;
its readiness assessment remains invalidated by the product instruction correction.
Documentation reassessment: complete with an evidenced no-change decision against
the corrected accepted implementation. Documentation review: pass for exact input
`75773f8bb5b4d055de5418fea74504b54431c2b7`; assessed README and no-change rationale.
Stage: all three review gates valid; ready for root delivery checks.

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

## Documentation evidence

Input: `a5f502a5de98e5b69de489875895f995d2dd3a86`. Assigned absolute path,
branch and exact HEAD matched; tracked/untracked status was empty before writing.
Used task-document and docbook; README is the established package introduction
and practical usage guide. No extra documentation scaffold is useful for this
scoped instruction-only package update.

Updated README to list nine skills, the specification planning through three
reviews and PR flow, useful minimal missing spec/docs creation, capability/rule
references instead of copied acceptance, separate author/reviewer write boundaries,
mandatory documentation/no-change assessment and review, documentation commit
prefixes, retained artifact-based gate validity, upstream routing and three-gate
delivery. Workflow installation now requires all seven task skills and both
specialists together with sibling layout; individual specialist installation,
marketplace commands and package identity are preserved. Invocation example follows
the implemented flow. Links point to the role protocol and gate rules for details.

At the prior documentation input, earlier passes remained valid: objective/scope,
acceptance, plan and verification content was unchanged against plan input
`87320f51efbe996cf396b17a6179fd0c1e7ed2ac`.
`git diff --exit-code 47bb45808da207cd855346e4c89c8fc259436af8 -- skills plugin.json`
confirmed all assessed implementation files/metadata unchanged. Only README and
this note changed; no implementation, test or contract edit occurred.

Package validator passed: nine frontmatters, 35 local links/anchors, metadata
0.3.0 / Repository Skills and preserved specialist/catalog bytes. `git diff
--check` passed. Read all seven implemented task skills and metadata against the
README claims. No source discrepancy or unresolved decision found. Documentation
review is independent and pending; no behavioral fixture or live publication
result is claimed by this role.

## Implementation correction evidence

Input: `5f37323a45d958fabf6fa9411328090dc978cb53`. Assigned absolute path,
branch and exact HEAD matched; tracked/untracked status was empty before writing.
Root's behavioral fixture observed a documenter notice missing reviewed-plan
artifact evidence but draft documentation before returning blocked. Tightened
task-document's precondition to inspect prerequisites and discrepancies before
documentation writes and return a committed note-only blocker/upstream route for
missing/stale passes or code/contract corrections. Independent investigation stays
read-only until required upstream passes; documentation-only defects remain in
the documenter's scope. Entry mismatches still stop without writes.

Only task-document product instructions and this note changed; README untouched.
Plan pass and exact reference `87320f51efbe996cf396b17a6179fd0c1e7ed2ac` remain
valid: objective/scope, acceptance, plan and verification are unchanged. Prior
implementation reference `47bb45808da207cd855346e4c89c8fc259436af8` and historical
review evidence are retained, but its assessed product instructions changed, so
that pass and downstream readiness are invalid. Ready for independent
implementation review of this correction's exact commit; documentation reassessment
and review follow its pass. No reviewer verdict is claimed here.

Validation: nine frontmatters, 35 local links/anchors, package metadata and
preserved specialist/catalog bytes passed the package validator; diff --check
passed. Behavioral recheck belongs to root; no new fixture or publication result
is claimed. No unresolved implementation decision.


## Corrective implementation review findings and evidence

Verdict: **pass** for exact input
`05a0fe89defb8bcee8f1b90404051cddc6ec1716`. No blocking finding or missing
material decision. Verified assigned absolute worktree, branch, clean tracked and
untracked status, and exact input HEAD before writing. This reviewer edits only
the task note; its commit is distinct from the reviewed input.

Assessed current product files: `skills/task-orchestrate/SKILL.md`,
`skills/task-plan/SKILL.md`, `skills/task-review-plan/SKILL.md`,
`skills/task-implement/SKILL.md`, `skills/task-review-implementation/SKILL.md`,
`skills/task-document/SKILL.md`, `skills/task-review-documentation/SKILL.md`, and
`plugin.json`. Read preserved specialist skills and current README as context.
Compared the note with accepted plan input
`87320f51efbe996cf396b17a6179fd0c1e7ed2ac`: objective/scope, acceptance, plan and
verification are unchanged, so that plan pass remains valid. Against prior
implementation input `47bb45808da207cd855346e4c89c8fc259436af8`, the only product
change is the reviewed task-document guard; other changes are README and note.

The guard orders prerequisite and discrepancy inspection before documentation
writes. Missing or stale retained plan/implementation passes and discrepancies
requiring code/contract correction explicitly return a committed note-only blocker
with upstream routing before documentation edits. Independent investigation stays
read-only until required passes; documentation-only defects remain authorized.
Entry-path/branch/HEAD or dirty-state mismatch still stops while preserving changes.
The later general documentation instructions do not override this precondition.
This resolves the recorded premature-documentation finding at source level.

Rechecked all implementation acceptance: affected contracts use specbook and named
rule coverage; author/reviewer write boundaries and actual-content classification
are explicit; documentation and independent review always follow implementation
pass, including committed no-change decisions. All three exact gate records and
artifact-based validity survive bookkeeping descendants, while substantive changes
invalidate affected/downstream gates. Useful minimal spec/docs creation, sequential
fresh-context roles, isolation, dirty handoff, stalled-loop, decisions, failed
delivery and clean cleanup behavior remain required. Delivery waits for three
valid passes. Version 0.3.0 and Repository Skills identity are preserved.
The prior installation advisory is addressed in README (seven task skills plus
both specialists together), but its downstream assessment must still be rerun.
Package-specific no-new-spec/README-only decisions remain scoped to this task.

Independent focused run of `work/validate_package.py <worktree> 0.3.0` passed:
nine frontmatters, 35 local links/anchors, preserved specialist/catalog bytes,
metadata identity/version and diff check. Base-to-input `git diff --check` also
passed. Read the existing Git lifecycle fixture evidence: ten passes, explicitly
limited to local delivery simulation and Git mechanics.

Limits: this review verifies product instructions and static/Git evidence; it does
not claim fresh execution of the behavioral recheck or live hosted publication.
Root owns that behavioral evidence. Documentation reassessment and its independent
review remain pending, so this pass does not approve delivery. No unresolved
implementation issue remains.


## Documentation reassessment evidence

Input: `1b6bd4b2cb74ca8d442ced1435da704fc4a5c601`. Verified assigned absolute
worktree, branch, exact HEAD and empty tracked/untracked status before writing.
Used task-document and docbook. Before documentation writes, confirmed retained
plan and implementation passes remain valid and inspected current sources for
code/contract discrepancies. No upstream discrepancy or missing decision found.

No-change decision: README already accurately describes all nine skills and seven
workflow roles; specification planning and independent documentation review; all
seven task skills plus specbook/docbook installed together in sibling layout;
three valid delivery gates; committed/reviewed documentation no-change decisions;
actual-content write boundaries; upstream correction routing; and retained exact
review references with artifact-based validity. Read all seven current task skill
entrypoints and plugin.json against these claims. The corrected task-document
precondition adds ordering and note-only blocking detail consistent with README's
accepted-implementation prerequisite and linked role/gate rules; it does not make
README guidance obsolete. No additional docs/scaffold is useful in this scoped
instruction-only package task. README therefore needs no edit.

Plan reference `87320f51efbe996cf396b17a6179fd0c1e7ed2ac` remains valid:
objective/scope, acceptance, plan and verification sections are unchanged in the
note diff. Current implementation reference
`05a0fe89defb8bcee8f1b90404051cddc6ec1716` remains valid: comparison of skills/
and plugin.json produced no diff. Historical implementation reference
`47bb45808da207cd855346e4c89c8fc259436af8` and prior documentation completion
`5f37323a45d958fabf6fa9411328090dc978cb53` retain their recorded invalidity after
the instruction correction. This reassessment replaces the stale documentation
readiness; it does not claim an independent documentation pass.

Focused package validation passed: nine frontmatters, 35 local links/anchors,
metadata 0.3.0 / Repository Skills, preserved specialist/catalog bytes, and diff
check. Only this task note changed; README, implementation, tests and contracts
remain untouched. Stage: ready-docreview. Independent documentation review is
pending. Behavioral fixtures and live publication remain root-owned; no new
behavioral or hosted delivery result is claimed. Open issues: none.

## Documentation review findings and evidence

Verdict: **pass** for exact input
`75773f8bb5b4d055de5418fea74504b54431c2b7`. No blocking finding or missing
material decision. Verified absolute worktree, task branch, exact HEAD and empty
tracked/untracked status before writing. This reviewer changes only this note;
its later commit is distinct from this reviewed documentation input.

Assessed README.md and the Documentation reassessment evidence/no-change rationale
against all seven current task skill entrypoints, preserved specbook/docbook,
plugin.json and marketplace metadata. README accurately lists nine skills,
explains specification planning and all three reviews, role write boundaries,
mandatory committed/reviewed no-change documentation, artifact-based gate validity,
upstream correction routing, sequential fresh-context handoffs and recoverable PR
delivery. Installation requires all seven task skills plus both specialists with
sibling paths; the earlier installation advisory is resolved. Package tree,
marketplace/display identities, skill invocation examples, relative links and
role/gate anchors match current sources. No missing asset or template content found.
Existing marketplace command examples were inspected as retained package guidance;
no plugin install or hosted action was executed in this review.

Independently accept the no-change reassessment: README is byte-identical to prior
documentation completion `5f37323a45d958fabf6fa9411328090dc978cb53`. The corrected
task-document guard adds prerequisite ordering and note-only upstream blocking,
consistent with the README's accepted-implementation prerequisite and linked
protocol/gate details. It introduces no obsolete README claim requiring another
edit. README remains the established introduction/usage guide; the accepted scoped
README-only decision avoids useless docs scaffolding and does not exempt general
workflow tasks from useful spec/docs creation or either specialist's rules.

Retained plan input `87320f51efbe996cf396b17a6179fd0c1e7ed2ac` remains valid:
inspected its full note diff; objective/scope, acceptance, plan and verification
are unchanged. Current implementation input
`05a0fe89defb8bcee8f1b90404051cddc6ec1716` remains valid: actual diff of skills/
and plugin.json is empty, and the entire descendant path diff contains only this
note. Historical implementation input
`47bb45808da207cd855346e4c89c8fc259436af8` retains its recorded invalidity after
the product instruction correction. Prior documentation readiness remains superseded
by reassessment and this independent review. All three current exact reviewed
references and assessed-artifact validity records are retained separately.

Independent `work/validate_package.py <worktree> 0.3.0` passed nine frontmatters,
35 local links/anchors, preserved specialist/catalog bytes, metadata identity and
version, and diff check. Base-to-input git diff --check passed. Read existing Git
lifecycle verification.json: ten passes limited to Git mechanics/local delivery.
Root separately reports external behavior fixtures for useful spec creation,
plan/docs reject-correct-re-review, early/stale prerequisite note-only stops,
code-discrepancy routing to implementation and undefined-policy routing to planning.
Those are root-supplied observations, not executions performed by this reviewer;
root's independent no-change and code-fix fixtures were still running at assignment.
This review claims local source/artifact/static evidence only, not those unfinished
external checks or live hosted publication. Root must resolve its delivery checks
before publication; no documentation issue remains open.
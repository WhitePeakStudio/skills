# Task note state

## Minimal working content

At every write, replace the entire bookkeeping prose outside the two marker-bounded
assessment blocks, not just your role's paragraph. Only those blocks and YAML
review receipts carry protected assessments; historical role narratives do not.
Keep one current note:

- Contract block: objective/scope, capability paths and rule names, task-specific
  acceptance not already owned by specifications, current implementation steps,
  documentation impact and verification commands. Reference authoritative
  acceptance instead of copying it. No plans or decision history in specifications.
- Documentation block: concise artifact assessment and affected paths, or an
  evidenced no-change rationale. No workflow status or role narrative.
- Outside blocks: current actionable findings/advisory dispositions, concise
  verification command/result/limits tied to input SHA, active resource constraints,
  and one resolved model map. Review inputs/paths already live in YAML; findings
  commits and previous executions live in Git.

For newly verified output, identify its handoff in the evidence; the return's
Commit/Git history supplies its SHA. Do not add a commit just to self-reference it.

Replace superseded/resolved detail. Retain evidence and dispositions still relevant
to acceptance or an unresolved issue, not transcripts, repeated checkout/signing
checks, loaded-file inventories, investigation chronology, per-role handoff summaries
or copied contracts. Routine confirmations stay in subagent context/return, not the note.
Do not compact accepted assessment blocks without reopening affected gates;
shorten bookkeeping alone when approvals must remain valid.

## YAML and receipts


Use YAML frontmatter in the existing `.task/<id>.md`. No execution array or separate
report: replace current records; Git commits retain every prior attempt and pass.

```yaml
---
task: example-a1b2c3d4
branch: task/example-a1b2c3d4
base: <full-base-sha>
stage: plan
reviews:
  plan: null
  implementation: null
  documentation: null
blocker: null
decision: null
recovery: null
---
```

Each latest review is `{verdict: pass|revise|needs-decision, input: <full-sha>,
artifacts: [literal/repository-relative/files]}`. `input` is the reviewer's assigned
HEAD, not its findings commit. The reviewer commits immediately on that HEAD with
its `review-…:` prefix; Git supplies the findings commit without a self-referencing
SHA field. `artifacts` lists files whose unchanged contents preserve approval,
not every file consulted. Typical selections:

- Plan: affected specifications and stable constraints.
- Implementation: implementation/tests and contract dependencies.
- Documentation: documentation and the code/specifications supporting its claims.

Treat planned downstream edit targets as context unless approval depends on their
current contents. If it does, include them and rerun the affected gate after changes;
never exclude a required dependency merely to keep a pass valid. Keep paths precise
and include additions/deletions. Empty lists are valid only for an
evidenced no-file-change assessment. The checker cannot prove scope completeness
or reviewer identity/correctness; reviewers remain responsible for those judgments.

Put objective, scope, acceptance, plan, and authoritative references between
`<!-- task-contract:start -->` and `<!-- task-contract:end -->`. Put documentation
assessment/no-change rationale between `<!-- task-documentation:start -->` and
`<!-- task-documentation:end -->` (initially empty). Keep evidence, findings,
and model selections outside those blocks. Compare block text exactly;
even whitespace edits require reassessment. Bookkeeping outside them does not.

All gates assess the contract block; documentation also assesses the documentation
block. Other assessed files are compared by Git object and mode at the reviewed SHA
and current HEAD. Unchanged descendants preserve passes; relevant changes invalidate
the affected gate and downstream gates. Clear downstream records when upstream
correction is required; keep valid unaffected records. A new review replaces its
own latest record; authors never manufacture review passes.
Downstream review inputs must retain the current upstream approval records and
descend from their findings commits. Renewed upstream approvals therefore require
fresh downstream reviews; a restored file alone cannot bypass that sequence.

An active blocker is `{id: stable-name, attempts: 0, evidence: [references]}`.
Increment attempts only after a corrective attempt leaves that blocker unresolved.
Do not reset by renaming it or changing stages. Agent judgment establishes blocker
identity and materially new evidence; record why before resetting the count when
new evidence changes the correction basis. Resolve the blocker to null when fixed.
`decision` is null or the material question; `recovery` is null or the interrupted
role name. Both non-null markers block normal progression. Explicit recovery follows
the shared protocol, outside normal checker permission, and clears its marker only
after reconciliation and a clean committed handoff.

The checker requires current `stage` to match `--action`, branch/task identity,
exact HEAD, clean tracked/untracked status, committed state, ancestor references,
review provenance in Git history, and valid prerequisite passes. Planning/review-plan
need no earlier pass; implementation/review-implementation need plan; documentation/
review-documentation need plan+implementation; delivery needs all three.
Review dispatch and passing review inputs must be the corresponding author's
handoff commit (`plan:`, `implement:`, `document:`), with stage set to that review.
Documentation assessment must be nonempty even for no-change tasks. This checks
commit provenance, not authorship identity or assessment quality.

# Repository Skills

An Agent Plugins package for issue intake/refinement, specifications, documentation,
isolated repository tasks, and skill optimization, with an optional token-counting
script.

## Custom agents

The plugin also supplies eight Copilot profiles in `com.github.copilot/agents/`:
`generic`, `task-orchestrate`, and the six task roles. Select `generic` for scoped
standalone work or `task-orchestrate` for the reviewed repository workflow.
Task-role profiles are available for delegation; workflow procedures stay in skills.

Edit the compact role definitions in [studio.whitepeak/agents.json](studio.whitepeak/agents.json)
and shared [organization guidance](studio.whitepeak/organization.md), then run:

```sh
python scripts/build-agents.py
python scripts/build-agents.py --check
```

Commit the generated profiles with their sources. Generation prepends the guidance
once to every profile; clients do not need prompt imports or shared inheritance.
The guidance applies to these WhitePeakStudio agents, not to every consumer of the
generic skills. Installing the plugin makes profiles available; it does not select
an agent automatically or grant permissions.

The source supports a description, prompt, and optional Copilot `model`. Omitted
models use Copilot's selection. Agent-runner translates the generated descriptions
and prompts into OpenCode; its deployment model/reasoning bindings remain authoritative,
including general-agent mention/label overrides. Copilot model names are not
translated to OpenRouter IDs. Runner tools, delegation, fresh contexts and environment
policy remain runner-owned; v1 rejects profile tool/MCP/handoff declarations.

Use the same pinned plugin revision for a job and its subagents. Organization
guidance changes do not alter workflow ownership, repository specifications or
the authorization of an individual request.

- [specbook](skills/specbook/SKILL.md): Authoritative capability specifications
  in `spec/`, with normative rules and observable acceptance criteria.
- [docbook](skills/docbook/SKILL.md): Documentation in `docs/`, with Diátaxis
  guidance, folder and page templates, and maintenance rules.
- [skill-optimize](skills/skill-optimize/SKILL.md): Standalone skill compression
  with comparable token measurements and checks for preserved meaning.
- [issue-create](skills/issue-create/SKILL.md): Capture requests as backlog issues
  or drafts, respecting repository ownership and avoiding duplicates.
- [issue-refine](skills/issue-refine/SKILL.md): Research and clarify issues, split
  coherent deliveries when needed, and prepare actionable leaves as Ready.
- [issue-execute](skills/issue-execute/SKILL.md): Execute scoped standalone issue
  work and return observed evidence for review.
- [task-orchestrate](skills/task-orchestrate/SKILL.md): Coordinate isolated tasks
  through fresh-context roles and pull-request delivery.
- [task-plan](skills/task-plan/SKILL.md): Write affected specifications and the
  implementation plan using specbook.
- [task-review-plan](skills/task-review-plan/SKILL.md): Independently review the
  exact plan commit.
- [task-implement](skills/task-implement/SKILL.md): Implement the accepted plan
  and record verification evidence.
- [task-review-implementation](skills/task-review-implementation/SKILL.md):
  Independently review the exact implementation commit.
- [task-document](skills/task-document/SKILL.md): Update documentation using
  docbook, or record an evidenced no-change decision.
- [task-review-documentation](skills/task-review-documentation/SKILL.md):
  Independently review the exact documentation commit or no-change decision.

The skills complement each other: specifications define required behavior;
documentation explains how to use, understand, develop, and operate the system.
Skill optimization works independently of the task workflow: it proposes a
compact revision, or edits the source when requested. It reports the tokenizer,
measurement scope, savings and verification; unavailable exact counts are explicit.

## Issue preparation

Use `issue-create` to capture, then `issue-refine` to prepare work. Follow existing
repository conventions: early ideas can be project drafts; cross-repository
initiatives live in the planning repository with implementation children in their
target repositories; single-repository work stays in that repository. Resolve
destinations/project from instructions and context, not hardcoded personal IDs.

The issue brief holds Outcome, Scope, Acceptance, and Context. Refinement researches
only relevant sources and splits independently verifiable deliveries, not workflow
roles. Native parent/child relationships and blocking dependencies remain distinct.
Only actionable leaves with clear requirements and satisfied dependencies become
`Ready`; unresolved work stays `Backlog`. Refinement returns URLs and never starts
implementation or approves a specification/implementation plan.

Explicitly give a Ready issue URL to `task-orchestrate`. It records one private execution association,
uses the existing worktree and three-review flow, and keeps `In progress` through
internal loops. A linked PR moves the item to `In review`; only observed merge or
explicit user acceptance permits `Done`/completed closure on a follow-up. Resume
recorded work rather than starting another task. Issue changes use normal contract
correction/review. V1 assumes one dispatcher, without automatic queue selection,
distributed locking, merge monitoring, or additional project fields/statuses.
Execution/worktree bookkeeping stays in task notes, Git, and runner state. Issue
comments contain only answers, PR links, questions, and actionable blockers.
See the conditional [issue handoff](skills/task-orchestrate/references/issues.md).

## Issue workflow labels

Use exactly one existing label before Ready: workflow:task selects task-orchestrate
for repository changes; workflow:agent selects a general agent using issue-execute
for standalone research, analysis, issue management, or explicitly requested
operations. Missing, conflicting, or unsupported workflow labels prevent runner
enrollment. Creation/refinement selects the label when intent is clear, not the
next issue to execute.

The runner posts a general agent's verified result summary and moves the item to
In review; explicit acceptance permits Done. No PR or task review stages are
required for this route. General agents do not modify repository content or bypass
the task workflow. They use a basic temporary environment with persistent scratch
data, fresh sessions, existing credentials, and no implicit privilege expansion.
Direct issue-execute invocation returns its result to the caller.

Vaka mentions in issue or Discussion comments can invoke the same general agent.
Each explicit request starts with fresh context and receives a reply; it requires
no Ready enrollment and changes no project status. The publishing harness owns
replies, with no execution or progress comments. Repository changes still require
the task workflow.

## Task workflow

The orchestrator creates one `task/<id>` branch and sibling `<repo>-tasks/<id>`
worktree, where `<id>` is `<short-kebab-slug>-<8-random-hex>`. Independent tasks
can run concurrently in separate checkouts. Within each task, fresh-context
subagents run sequentially: specification planning, plan review, implementation,
implementation review, documentation, documentation review, then PR delivery.
Each role verifies the assigned clean path, branch, and input commit,
then commits before the next handoff. This workflow requires fresh-context
subagent support; the package provides instructions, not an orchestration service.

Interrupted work is recovered by the same role in fresh context only after its
previous writer has stopped and its changes have been identified. Normal handoffs
remain clean; uncertain ownership requires reconciliation. Runtime resources
outside the checkout need task-specific isolation or coordinated exclusive use.

The orchestrator prefers GPT-6 Luna for documentation and its review, and GPT-6.1
Sol for the other roles. Explicit task instructions override these defaults.
Model identifiers are resolved through the host; unavailable built-in preferences
fall back to the host default with disclosure, while unsupported explicit choices
require a decision. Reasoning effort inherits host settings unless specified.
See [subagent models](skills/task-orchestrate/SKILL.md#subagent-models).

Planning uses specbook to write affected capability contracts in `spec/`; task
acceptance and verification reference capability paths and rule names instead of
duplicating the contracts. Missing spec or documentation structures receive only
the useful content needed for the task, without empty scaffolds or unrelated
migrations. A task needing no contract change records its reason.

Authors have separate write boundaries: planner writes specifications and the
note; implementer writes authorized implementation/tests and the note; documenter
writes documentation, README, documentation examples/assets and the note. Every
reviewer writes only the note. Classify files by their actual content: product
instructions such as these SKILL.md files are implementation. Documentation
assessment and independent review are mandatory after accepted implementation,
even when the result is a committed, evidenced no-change decision. Documentation
commits use `document:` and review commits use `review-documentation:`. See the
[role protocol](skills/task-orchestrate/references/role-contract.md) for all role prefixes
and handoff requirements.

Blocking findings return to the responsible author for correction and fresh
review. Contract or plan changes return to planner/plan reviewer; code defects
return to implementer/implementation reviewer; documentation defects return to
documenter/documentation reviewer. Upstream corrections require fresh documentation
assessment and review against the corrected accepted artifacts.

Reviewers retain each gate's exact reviewed SHA and assessed artifacts separately
from their own note commit. Earlier passes remain valid on descendants only while
those artifacts, including assessed plan/acceptance content, are unchanged;
substantive changes invalidate the affected gate and downstream assessments.
Documentation or bookkeeping alone can preserve unchanged earlier passes; Markdown
product instructions have no blanket exemption. See the
[gate rules](skills/task-orchestrate/references/gates.md).
Accounted-for advisories do not block acceptance. Missing decisions pause dependent
work, and the same blocker after two corrective attempts without new evidence ends
the loop.

Each reviewer examines cumulative changes in its scope from the recorded task
base to the assigned commit, including corrections. Reviewers assess requirements
and artifacts independently before comparing author-provided evidence; the task
note holds facts rather than reasoning transcripts.

One compact `.task/<id>.md` holds current scope, acceptance, plan, stage,
findings/evidence, and decisions. Replace stale state instead of accumulating
logs. Handoffs supply path/branch, objective/scope, exact input commit/sources,
and acceptance/expected result. Roles return only Status, Commit, Result,
Evidence, and Open issues; assignment completion and review verdict are distinct.

Roles load their own skill, the short shared role contract and note state, plus
relevant artifacts/specialist instructions. Recovery and delivery references are
loaded only when needed; the orchestrator does not preload every role. Keep note
prose to current findings and concise command/result evidence tied to commits;
omit role narratives and routine check logs. YAML alone owns workflow status.

The note's compact YAML records identity/base, next stage, latest review inputs and
assessed paths, current blocker/attempts, decision, and recovery marker. Git history
retains repeated executions. Bounded contract and documentation-assessment blocks
separate reviewed content from changing bookkeeping. The read-only Python gate
checker verifies local prerequisites before dispatch/delivery and returns only
`allowed`/`reason`; it neither selects corrective routes nor proves review quality
or hosted verification. See the [gate contract](skills/task-orchestrate/references/gates.md)
for exhaustive transitions, setup, and invocation; [note state](skills/task-orchestrate/references/state.md) defines the unchanged format. It requires PyYAML
only when running the checker. Missing prerequisites block normal progression;
explicit interrupted-role recovery remains governed by the shared protocol.

Delivery requires valid passing plan, implementation, and documentation gates.
Default delivery removes the note in a delivery commit, preserves role history,
verifies a clean checkout and zero task-note net diff, pushes without force, and
opens a PR. Delivery fetches and reports target-branch movement without automatic
integration. Hosted mergeability and relevant CI are checked at the pushed head:
failed checks or conflicts block completion; pending or unavailable results mean
**PR opened, verification pending**. No configured CI is not a CI pass. There is
no indefinite polling or automatic monitoring. Keep the worktree until applicable
verification and mergeability are resolved; a later invocation can resume from
the existing PR, branch, and committed task history. Required attachment also
precedes clean worktree removal; branch/history remain. Integration or corrective
changes reopen affected gates. User instructions can select another delivery
method; role subagents never push or open PRs.

## Package layout

```text
plugin.json
skills/
|-- specbook/SKILL.md
|-- docbook/SKILL.md
|-- skill-optimize/SKILL.md
|-- issue-create/SKILL.md
|-- issue-refine/SKILL.md
|-- issue-execute/SKILL.md
|-- task-orchestrate/SKILL.md
|-- task-orchestrate/references/gates.md
|-- task-orchestrate/references/issues.md
|-- workspace.md
|-- task-orchestrate/scripts/check_gate.py
|-- task-plan/SKILL.md
|-- task-review-plan/SKILL.md
|-- task-implement/SKILL.md
|-- task-review-implementation/SKILL.md
|-- task-document/SKILL.md
`-- task-review-documentation/SKILL.md
.agents/plugins/marketplace.json
```

The root manifest uses the [Agent Plugins schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json).
All thirteen skills are discovered from `skills/`. OpenAI presentation metadata lives in
`extensions.com.openai`; the repository also includes a Codex marketplace catalog.
The package requires no MCP servers. Issue skills and issue-based orchestration
require authenticated `gh` with access to the selected repositories/project;
`gh api` covers capabilities absent from installed CLI commands. They discover
existing field IDs and verify partial updates before retrying. Direct task inputs
do not load issue guidance. The task gate checker uses
Python 3.10+, Git, and PyYAML. The optional skill-optimize
token-counting script uses Python 3.10+ and `tiktoken`; its setup and usage
are in the skill. It accepts arbitrary text, files, or stdin independently of
repository layout. It measures text, not behavioral equivalence, and may
download tokenizer data on first use.

## Install in Codex

Add the repository marketplace:

```sh
codex plugin marketplace add WhitePeakStudio/skills
```

For a local checkout, run this command from its root instead:

```sh
codex plugin marketplace add .
```

Then open the Plugins Directory, select **WhitePeakStudio Skills**, and install
**Repository Skills**. See the [OpenAI plugin packaging guide](https://developers.openai.com/plugins/build/plugins)
for marketplace and installation details.

## Use

Select the relevant skill in your agent, or request it by name:

```text
Use specbook to review the authentication capability in spec/.
Use docbook to organize the existing documentation in docs/.
Use skill-optimize to shorten this skill, compare token counts, and preserve its instructions.
Use issue-create to capture this request in the supplied project's Backlog, following its repository conventions.
Use issue-refine on <issue-url> (or <project-url> and <draft-item-id>), and return eligible Ready issue URLs.
Use task-orchestrate to implement the Ready issue at <issue-url> in its target repository.
Use task-orchestrate to deliver this repository change through specification planning, implementation, documentation, and all three reviews to a PR.
```

Hosts that support portable Agent Plugins can load the root package. Standalone
skill installers can install `skills/specbook`, `skills/docbook`, or
`skills/skill-optimize`, `skills/issue-create`, or `skills/issue-refine` individually.
The two issue skills operate independently; installing them does not install the
task workflow. Skill optimization has no sibling skill
dependencies; exact counting uses a tokenizer available on the host.
For the task workflow, install all seven `task-*` skills plus `specbook` and
`docbook` together, preserving their sibling directory layout for relative links.
Include `skills/workspace.md` alongside the skill directories for `task-orchestrate`
and `issue-execute`. It owns the shared `repos/<owner>/<repository>/`, `tasks/<task-id>/`
and `temp/` conventions. Workspaces start empty when supplied by the harness; sources
do not require a clone. Clone only when needed and reuse verified work on resume.
Environment provisioning and physical storage remain harness responsibilities.
Specbook and docbook retain their existing instructions
and replace the previous top-level paths.

## Maintain

Edit each skill's `SKILL.md` and keep its frontmatter name aligned with its folder.
For releases, update `version` in `plugin.json`. Keep the marketplace entry's name
aligned with the plugin manifest, and its source path relative to the repository
root.

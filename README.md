# Repository Skills

An instructions-only Agent Plugins package for specifications, documentation,
and isolated repository tasks.

- [specbook](skills/specbook/SKILL.md): Authoritative capability specifications
  in `spec/`, with normative rules and observable acceptance criteria.
- [docbook](skills/docbook/SKILL.md): Documentation in `docs/`, with Diátaxis
  guidance, folder and page templates, and maintenance rules.
- [task-orchestrate](skills/task-orchestrate/SKILL.md): Coordinate isolated tasks
  through fresh-context roles and pull-request delivery.
- [task-plan](skills/task-plan/SKILL.md): Write or correct the implementation plan.
- [task-review-plan](skills/task-review-plan/SKILL.md): Independently review the
  exact plan commit.
- [task-implement](skills/task-implement/SKILL.md): Implement the accepted plan
  and record verification evidence.
- [task-review-implementation](skills/task-review-implementation/SKILL.md):
  Independently review the exact implementation commit.

The skills complement each other: specifications define required behavior;
documentation explains how to use, understand, develop, and operate the system.

## Task workflow

The orchestrator creates one `task/<id>` branch and sibling `<repo>-tasks/<id>`
worktree, where `<id>` is `<short-kebab-slug>-<8-random-hex>`. Independent tasks
can run concurrently in separate checkouts. Within each task, fresh-context
subagents run sequentially: plan, plan review, implementation, implementation
review. Each role verifies the assigned clean path, branch, and input commit,
then commits before the next handoff. This workflow requires fresh-context
subagent support; the package provides instructions, not an orchestration service.

Blocking findings return to the corresponding author and receive a fresh review
of the corrective commit. Scope or plan changes re-enter plan review. Reviewers
record the reviewed SHA separately from their own note commit; accounted-for
advisories do not block acceptance. Missing decisions pause dependent work, and
the same blocker after two corrective attempts without new evidence ends the loop.

One compact `.task/<id>.md` holds current scope, acceptance, plan, stage,
findings/evidence, and decisions. Replace stale state instead of accumulating
logs. Handoffs supply path/branch, objective/scope, exact input commit/sources,
and acceptance/expected result. Roles return only Status, Commit, Result,
Evidence, and Open issues; assignment completion and review verdict are distinct.

Default delivery removes the note in a delivery commit, preserves role history,
verifies a clean checkout and zero task-note net diff, pushes without force, and
opens a PR. Required PR attachment precedes clean worktree removal; the branch
and history remain. Failed delivery retains recoverable state. User instructions
can select another delivery method; role subagents never push or open PRs.

## Package layout

```text
plugin.json
skills/
|-- specbook/SKILL.md
|-- docbook/SKILL.md
|-- task-orchestrate/SKILL.md
|-- task-plan/SKILL.md
|-- task-review-plan/SKILL.md
|-- task-implement/SKILL.md
`-- task-review-implementation/SKILL.md
.agents/plugins/marketplace.json
```

The root manifest uses the [Agent Plugins schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json).
All seven skills are discovered from `skills/`. OpenAI presentation metadata lives in
`extensions.com.openai`; the repository also includes a Codex marketplace catalog.
The package contains instructions only and requires no MCP servers or credentials.

## Install in Codex

Add the repository marketplace:

```sh
codex plugin marketplace add jb-perrier/skills
```

For a local checkout, run this command from its root instead:

```sh
codex plugin marketplace add .
```

Then open the Plugins Directory, select **jb-perrier Skills**, and install
**Repository Skills**. See the [OpenAI plugin packaging guide](https://developers.openai.com/plugins/build/plugins)
for marketplace and installation details.

## Use

Select the relevant skill in your agent, or request it by name:

```text
Use specbook to review the authentication capability in spec/.
Use docbook to organize the existing documentation in docs/.
Use task-orchestrate to implement this repository change with plan and implementation reviews.
```

Hosts that support portable Agent Plugins can load the root package. Standalone
skill installers can install `skills/specbook` or `skills/docbook` individually.
For the task workflow, install all five `task-*` skills together, preserving their
sibling directory layout. Specbook and docbook retain their existing instructions
and replace the previous top-level paths.

## Maintain

Edit each skill's `SKILL.md` and keep its frontmatter name aligned with its folder.
For releases, update `version` in `plugin.json`. Keep the marketplace entry's name
aligned with the plugin manifest, and its source path relative to the repository
root.

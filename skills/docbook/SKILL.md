---
name: docbook
description: Rules and folder templates for writing, organizing, and reviewing repository documentation in docs/ using Diátaxis.
---

# Documentation

`docs/` explains how to use, understand, develop, and operate the system.
Organize content by reader need using [Diátaxis](https://diataxis.fr/start-here/).
Maintain documentation as code: versioned Markdown, reviewed alongside changes,
with the repository's documentation checks when available.

## Boundaries

When `spec/` exists, it owns required behavior and acceptance criteria. Link to
the relevant capability rather than duplicating normative rules in `docs/`.
Documentation describes current behavior and practical use. If code, specs, and
documentation disagree, report the discrepancy; do not silently redefine the
contract or describe intended behavior as implemented.

Keep the root README as the project introduction and link it to `docs/README.md`.
Keep plans, work logs, and temporary investigation notes outside maintained
documentation unless the repository explicitly gives them a home.

## Files

Use this default structure for new documentation:

```text
docs/
|-- README.md          Documentation entry point and index
|-- tutorials/         Guided learning experiences
|-- how-to/            Instructions for specific tasks
|-- reference/         Precise technical descriptions
|-- explanation/       Concepts, architecture, and rationale
|-- decisions/         Optional architectural decision records
`-- assets/            Images and diagrams referenced by pages
```

Create only directories and pages with useful content. Small documentation sets
can start with an index and a few pages. Preserve established organization when
it serves readers; adopting this skill alone does not require a migration.
The tree is a repository convention, not a mandatory Diátaxis layout.

Use one page per cohesive reader need, with descriptive lowercase hyphenated
filenames. Add a topic subfolder when it groups several related pages and
improves navigation. Reference hierarchy may follow the interface it describes;
other sections should follow reader tasks and concepts rather than code folders.

For multi-file documentation, `docs/README.md` MUST identify the audience and
provide an index grouped by purpose with relative links. Use this template,
omitting empty groups:

```markdown
# Documentation

Short description of the system and who this documentation serves.

## Start here

- [First steps](tutorials/first-steps.md): Learn the basic workflow.

## How-to guides

- [Configure the system](how-to/configure.md): Complete a specific task.

## Reference

- [Configuration](reference/configuration.md): Options and defaults.

## Explanation

- [Architecture](explanation/architecture.md): Components and tradeoffs.
```

Adapt the links to real pages. Keep details in their pages rather than repeating
them in the index. Link optional decision records when present.

## Page types

Choose the type before writing:

- **Tutorial:** Teach through a bounded, reproducible exercise. Give prerequisites,
  guided steps, and visible results. Keep choices and background limited.
- **How-to:** Help a competent reader achieve a specific goal. Include relevant
  prerequisites, steps, verification, and recovery where needed.
- **Reference:** Describe interfaces, commands, configuration, or data accurately.
  Use consistent entries covering applicable types, defaults, constraints,
  outputs, and errors. Identify generated material and update its source.
- **Explanation:** Explain concepts, relationships, reasons, and tradeoffs.
  Link to procedures and reference details rather than embedding them.

Split substantial content serving different needs into linked pages. Every page
needs a descriptive title and a short statement of purpose; other headings
depend on its type. Omit empty or irrelevant sections.

A how-to guide can start from:

```markdown
# Task name

What this guide achieves and when to use it.

## Prerequisites

Required access, tools, and initial state.

## Steps

1. Concrete action with the needed command or example.
2. Next action and any expected intermediate result.

## Verify

How to confirm the task succeeded and the expected outcome.

## Troubleshooting

Relevant failure symptoms and recovery actions.
```

## Decisions

When decision history is useful, follow existing conventions or use
`docs/decisions/NNNN-short-title.md`:

```markdown
# Decision title

## Status

Proposed, accepted, rejected, or superseded; date and replacement link if relevant.

## Context

Problem, constraints, and alternatives that matter.

## Decision

Chosen approach and reasons.

## Consequences

Benefits, costs, and follow-up implications.
```

Decision records preserve history. Supersede accepted decisions with linked
records when choices change; keep current architecture in `explanation/`.

## Editing

1. Read the affected pages, index, and relevant sources or specifications.
2. Choose the reader need and canonical page. Link to existing content instead
   of copying it; use relative links within the repository.
3. Update obsolete guidance and affected examples, navigation, and cross-links.
   State version or environment assumptions when they affect applicability.
4. Verify technical claims against available evidence. Check commands and
   examples where practical without performing unauthorized external actions.
   Mark unresolved gaps explicitly rather than inventing details.
5. Check broken links, missing assets, duplicate or conflicting text, and leftover
   template content. Run existing documentation checks when applicable. Report
   changes and any verification limits.

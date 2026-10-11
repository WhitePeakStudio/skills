---
name: docbook
description: Rules and folder templates for writing, organizing, and reviewing repository documentation in docs/ using Diátaxis.
---

# Documentation

`docs/` explains system use, understanding, development, and operation. Organize
by reader need using [Diátaxis](https://diataxis.fr/start-here/). Maintain versioned
Markdown, review alongside changes, and run available repository documentation checks.

## Boundaries

When `spec/` exists, it owns required behavior/acceptance; link capabilities instead
of duplicating normative rules. Document current behavior and practical use. Report
code/spec/docs discrepancies; never silently redefine contracts or present intended
behavior as implemented.

Keep root README as project introduction, linking `docs/README.md`. Plans, work
logs, and temporary investigations stay outside maintained docs unless the
repository explicitly provides a home.

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

Create only useful directories/pages; small sets can start with an index and a few
pages. Preserve organization that serves readers; skill adoption requires no migration.
This tree is a repository convention, not a mandatory Diátaxis layout.

Use one page per cohesive reader need, with descriptive lowercase hyphenated names.
Topic subfolders must group several related pages and improve navigation. Reference
hierarchy may follow interfaces; other sections follow reader tasks/concepts, not code folders.

For multi-file docs, `docs/README.md` MUST identify the audience and index pages
by purpose with relative links. Use this template; omit empty groups:

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

Link real pages and optional decision records when present; keep page details out of the index.

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

Split substantial distinct reader needs into linked pages. Require a descriptive
title and short purpose per page; other headings depend on type. Omit empty/irrelevant sections.

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

Preserve decision history: supersede changed accepted decisions with linked records;
keep current architecture in `explanation/`.

## Editing

1. Read the affected pages, index, and relevant sources or specifications.
2. Choose reader need/canonical page; link existing content rather than copying,
   using relative repository links.
3. Update obsolete guidance and affected examples/navigation/cross-links. State
   version/environment assumptions affecting applicability.
4. Verify claims against evidence; check commands/examples where practical without
   unauthorized external actions. Mark unresolved gaps; never invent details.
5. Check links, assets, duplicate/conflicting text, and leftover templates. Run
   applicable documentation checks; report changes and verification limits.

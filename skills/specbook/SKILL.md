---
name: specbook
description: Rules for writing and reviewing authoritative capability specifications in spec/.
---

# Specification

`spec/` is authoritative.

## Files

Use one self-contained `spec/<area>/.../<capability>.md` per cohesive capability
or cross-cutting concern. Default to one area level; subareas must group several
related capabilities and improve navigation. Never create a one-capability directory
or mirror implementation structure. Split independent capabilities; keep shared context.

For multi-file specs, `spec/README.md` MUST provide product scope, shared terminology,
and an area-grouped capability index with relative links. It supplies shared context,
not a capability:

```markdown
# Specification

Short product purpose.

## Scope

- Owns ...
- Excludes ...

## Terminology

- **Term:** Meaning.

## Capabilities

### Area

- [Capability](area/capability.md): Short purpose.
```

Keep rules/capability details in their files, not duplicated in the index.

A capability file uses:

```markdown
# Capability name

Short purpose and scope.

## Rules

- **Rule name:** The system MUST ...
- **Another rule:** The system MUST NOT ...
- **Optional rule:** The system MAY ...

## Acceptance

- **Rule name:** Observable conditions and expected outcome.
- **Another rule:** Observable conditions and expected outcome.
- **Optional rule:** Observable conditions and expected outcome.
```

Require description, `Rules`, and `Acceptance`. Every rule MUST have acceptance
coverage under the same short bold name. Each normative rule belongs to one
capability; related files link rather than restate it. Normative rules belong in
`Rules`; other sections supply referenced supporting detail, not independent obligations.

Acceptance states initial conditions, trigger/input, and observable outcome that
distinguish success/failure, not rule restatements or test implementation. Cover
applicable boundaries, invalid inputs, failures, and recovery. Given/When/Then is
optional. MAY rules cover both supported/enabled behavior and valid absent/disabled outcomes.

Other sections are optional; omit empty ones. Use MUST, MUST NOT, and MAY deliberately.
Keep implementation, plans, and chronological decisions outside `spec/`. Tests/
verification reference capability path and rule name for acceptance coverage;
no separate traceability document or numeric IDs required.

## Section vocabulary

Prefer these names when they fit:

- `Scope`: ownership, boundaries, exclusions.
- `Terminology`: capability-specific terms and meanings.
- `Rules`: required behavior and invariants.
- `Rationale`: reasons needed to understand current rules and tradeoffs.
- `Interface`: inputs, outputs, operations, contracts.
- `Data`: shapes, persistence, and retention.
- `Configuration`: settings, defaults, precedence, overrides.
- `Limits`: size, time, capacity, and resource bounds.
- `Lifecycle`: states and transitions.
- `Errors`: failures, effects, recovery.
- `Security`: authority, trust boundaries, sensitive data.
- `Compatibility`: versions, migration, deprecation, backward compatibility.
- `Operations`: status, diagnostics, monitoring, maintenance.
- `Interactions`: related capabilities with relative links.
- `Examples`: non-normative illustrations.
- `Acceptance`: observable conditions and expected outcomes covering rules.

Add a clear name when none fits; do not rename an existing concept without need.

## Editing

1. Read the whole capability and related files.
2. Ask one focused question if a material choice is unclear.
3. Replace obsolete behavior; update affected sections, capabilities, and index
   links.
4. Check stale, duplicate, conflicting, or out-of-scope text and broken links.
   Report changes and decisions.

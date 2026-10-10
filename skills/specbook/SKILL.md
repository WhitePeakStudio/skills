---
name: specbook
description: Rules for writing and reviewing authoritative capability specifications in spec/.
---

# Specification

`spec/` is authoritative.

## Files

Use one self-contained `spec/<area>/.../<capability>.md` per cohesive capability
or cross-cutting concern. One area level is the default. Add a subarea only when
it groups several related capabilities and improves navigation; never create a
directory for one capability or mirror implementation structure. Split
independent capabilities; keep shared context together.

For a multi-file specification, `spec/README.md` MUST provide the product scope,
shared terminology, and a capability index grouped by area with relative links.
It is shared context, not a capability file:

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

Keep rules and capability details in their files; do not duplicate them here.

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

Description, `Rules`, and `Acceptance` are required. Every rule MUST have
acceptance coverage. Give each rule a short bold name and reuse it in
`Acceptance`. Each normative rule belongs to one capability; related files link
to it rather than restating it. Put normative rules in `Rules`; other sections
provide supporting detail referenced by those rules, not independent obligations.

Acceptance gives enough initial conditions, trigger or input, and observable
outcome to distinguish success from failure; do not merely restate the rule or
describe test implementation.
Cover relevant boundaries, invalid inputs, failures, and recovery where applicable.
Given/When/Then is optional. For MAY rules, cover behavior when supported or
enabled and the valid outcome when absent or disabled.

Other sections are optional; omit them when empty. Use MUST, MUST NOT, and MAY
deliberately. Keep implementation, plans, and chronological decision history
outside `spec/`. In tests or verification reports, reference the capability path
and rule name so acceptance coverage can be checked; no separate traceability
document or numeric IDs are required.

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

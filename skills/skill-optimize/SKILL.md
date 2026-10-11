---
name: skill-optimize
description: Reduce the token cost of existing agent skills while preserving their instructions and behavior. Use for skill compression and before/after token measurement.
---

# Optimize a skill

Read the target SKILL.md and relevant referenced instructions. Keep an original
snapshot for comparison. Optimize the requested skill, not its requirements or
unrelated files. This skill is standalone; no task workflow or subagents required.
Present a proposed revision by default; edit the source when requested.

## Measure

Use an available tokenizer for the intended model, recording its name/encoding
and version. If unspecified, use an available named tokenizer and disclose that
choice. Count original and revised text with the same tokenizer, file set, and
text-reading method, preserving whitespace. Include frontmatter in file counts;
these measure instruction text, not host prompt overhead.

Report SKILL.md separately from referenced instructions; identify mandatory and
conditional loads. Count each file once in totals. Moving text to references is
deferred loading, not necessarily a reduction in total tokens. Do not count assets
or executable helpers as instructions unless their source is actually loaded.
If accurate counting is unavailable, state that limitation; label estimates and
do not claim exact savings. Do not install dependencies without authorization.

## Compress and verify

Identify the original triggers, prerequisites, required and optional actions,
ordering, write/permission boundaries, exceptions, outputs, failure behavior,
and supporting links. Preserve these invariants and frontmatter discovery meaning.
Remove repetition, shorten phrasing, and consolidate equivalent rules. Keep
conditions explicit, examples that clarify behavior, and readable language;
avoid cryptic shorthand or replacing precise rules with broad summaries.

Compare the revision against every original invariant, including referenced
instructions. Check realistic normal, exception, and blocked cases for changed
decisions. Token savings alone do not establish equivalence. Restore any wording
whose removal creates uncertainty; stop when further cuts weaken clarity or
behavior. No reduction quota applies, and an already compact skill may need none.
Do not hide or remove requirements by relocating or dropping linked resources.

For complex skills, an independent fresh-context review can add confidence when
available and authorized; give it original and revision without author reasoning.
It is optional. Keep working comparisons temporary; no permanent report required.

Return the revision or edited paths, tokenizer and measurement scope, before/after
counts, tokens saved and percentage (when baseline is nonzero), verification,
and unresolved uncertainty. Claim preserved meaning only to the extent checked.

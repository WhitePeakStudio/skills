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

The generic [count_tokens.py](scripts/count_tokens.py) counts arbitrary text using
Python 3.10+ and `tiktoken`. With authorization, install the dependency in your
chosen environment: `python -m pip install tiktoken`. The script never installs
it; the first encoding load may download tokenizer data, cached runs can be offline.

```sh
python scripts/count_tokens.py --text "Text to measure"
python scripts/count_tokens.py --file /path/to/instructions.md
```

Use the script's absolute path or run from this skill's directory. With neither
input option, it reads UTF-8 stdin. JSON reports token count, tokenizer/version,
and encoding. Whitespace/newlines are preserved; special-token-like strings are
literal text. Default `o200k_base` is a measurement encoding, not a target-model
claim; use `--encoding` to select another. Choose files, aggregate counts, and
compare revisions yourself; the script has no repository or skill-specific logic.

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

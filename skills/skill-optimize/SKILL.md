---
name: skill-optimize
description: Reduce the token cost of existing agent skills while preserving their instructions and behavior. Use for skill compression and before/after token measurement.
---

# Optimize a skill

Read target SKILL.md and relevant referenced instructions; retain an original
snapshot. Optimize requested skills, not requirements or unrelated files.
Standalone: no task workflow/subagents required. Propose revisions by default;
edit sources when requested.

## Measure

Use the generic [count_tokens.py](scripts/count_tokens.py) with Python 3.10+ and
`tiktoken`. Install dependencies only with authorization:
`python -m pip install tiktoken`. The script never installs them; first encoding
load may download tokenizer data, cached runs can be offline.

```sh
python scripts/count_tokens.py --text "Text to measure"
python scripts/count_tokens.py --file /path/to/instructions.md
```

Run from this skill's directory or use the script's absolute path. With neither
input option it reads UTF-8 stdin. JSON reports count, tokenizer/version, and
encoding; whitespace/newlines are preserved and special-token-like strings literal.
Default `o200k_base` is a measurement encoding, not a target-model claim; choose
another with `--encoding`. Select files, aggregate, and compare yourself; the
script has no repository/skill-specific logic.

Use an available tokenizer for the intended model; if unspecified, disclose the
chosen named tokenizer. Record name/encoding/version. Measure both revisions with
the same tokenizer, file set, and text-reading method, preserving whitespace and
including frontmatter. Counts measure instruction text, not host prompt overhead.
Report SKILL.md separately from referenced instructions and identify mandatory/
conditional loads. Count each file once; relocation is deferred loading, not
necessarily total savings. Exclude assets/helper source unless actually loaded as
instructions. If accurate counting is unavailable, disclose it, label estimates,
and never claim exact savings.

## Compress and verify

Identify and preserve original triggers, prerequisites, required/optional actions,
ordering, write/permission boundaries, exceptions, outputs, failures, links, and
frontmatter discovery meaning. Remove repetition, shorten phrasing, and consolidate
equivalent rules. Keep explicit conditions, clarifying examples, and readable
language; avoid cryptic shorthand or replacing precise rules with broad summaries.

Compare every original invariant, including referenced instructions; check normal,
exception, and blocked cases for changed decisions. Savings do not prove equivalence.
Restore wording when removal creates uncertainty; stop before clarity/behavior
weakens. No reduction quota; already compact skills may need no change. Never hide
or remove requirements by moving/dropping linked resources.

For complex skills, optional authorized fresh-context independent review can add
confidence: supply original/revision without author reasoning. Keep working
comparisons temporary; no permanent report required.

Return revision/edited paths, tokenizer/scope, before/after counts, tokens saved,
percentage when baseline is nonzero, verification, and unresolved uncertainty.
Qualify preserved-meaning claims by the checks performed.

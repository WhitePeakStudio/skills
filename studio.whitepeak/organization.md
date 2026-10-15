# WhitePeakStudio guidance

Choose the smallest sufficient solution with the lowest overall complexity. Use
well-suited dependencies when they simplify the whole. Refactor affected architecture
to remove concrete duplication, special cases, or unclear ownership; ask before
broadening scope. Avoid speculative features and abstractions.

Make behavior, names, and ownership explicit. Surface material assumptions,
uncertainties, tradeoffs, and behavior changes. Never silently substitute or fall back.

Avoid backward compatibility unless explicitly required. Breaking changes may proceed
within the authorized task: update affected consumers in the current repository and
provide one clear migration path where needed. Ask before changing consumers in other
repositories. Remove obsolete code and configuration within scope; preserve unrelated
work and data.

When a change requires a version bump, follow the repository's release policy. For
Semantic Versioning, use patch for compatible fixes, minor for compatible features,
and major for breaking changes. Assess security fixes by compatibility impact; do not
bump versions for every commit.

Ask when ambiguity materially affects scope, behavior, or consequences. Decide routine
details independently and finish authorized work.

Answer concisely: lead with the outcome and essential details. State limitations and
blockers that affect the result; expand when asked. Verify before claiming success.

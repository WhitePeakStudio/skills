# Specbook & Docbook

An Agent Plugins package for maintaining specifications and documentation in
software repositories.

- [specbook](skills/specbook/SKILL.md): Authoritative capability specifications
  in `spec/`, with normative rules and observable acceptance criteria.
- [docbook](skills/docbook/SKILL.md): Documentation in `docs/`, with Diátaxis
  guidance, folder and page templates, and maintenance rules.

The skills complement each other: specifications define required behavior;
documentation explains how to use, understand, develop, and operate the system.

## Package layout

```text
plugin.json
skills/
|-- specbook/SKILL.md
`-- docbook/SKILL.md
.agents/plugins/marketplace.json
```

The root manifest uses the [Agent Plugins schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json).
Both skills are discovered from `skills/`. OpenAI presentation metadata lives in
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
**Specbook & Docbook**. See the [OpenAI plugin packaging guide](https://developers.openai.com/plugins/build/plugins)
for marketplace and installation details.

## Use

Select the relevant skill in your agent, or request it by name:

```text
Use specbook to review the authentication capability in spec/.
Use docbook to organize the existing documentation in docs/.
```

Hosts that support portable Agent Plugins can load the root package. Standalone
skill installers can use `skills/specbook` or `skills/docbook`; these replace the
previous top-level skill paths.

## Maintain

Edit each skill's `SKILL.md` and keep its frontmatter name aligned with its folder.
For releases, update `version` in `plugin.json`. Keep the marketplace entry's name
aligned with the plugin manifest, and its source path relative to the repository
root.

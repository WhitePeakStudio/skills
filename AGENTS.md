# Repository instructions

## Generated custom agents

Edit `studio.whitepeak/organization.md` and `studio.whitepeak/agents.json` as the
sources; do not edit generated `com.github.copilot/agents/*.agent.md` files directly.
After changing either source or `scripts/build-agents.py`, run:

```sh
python scripts/build-agents.py
python scripts/build-agents.py --check
```

Commit the generated profiles with their source changes. CI checks freshness on
pushes and pull requests; it does not regenerate files.

# Shared workspace conventions

Use the harness-supplied workspace root, otherwise the initial working directory
(the checkout's parent when starting inside Git). Keep that root stable across directory changes.
An issue/Discussion source identifies context; it does not require a checkout.
Use APIs when sufficient and clone only for needed local inspection or execution.

Create only directories needed for the assignment, relative to that root:

- `repos/<owner>/<repository>/`: repository clones.
- `tasks/<task-id>/`: isolated task Git worktrees.
- `temp/`: disposable research files, downloads and intermediate outputs.

Before reuse or resume, inspect existing directories, remote identity, HEAD and
working-tree status. Reuse verified work; preserve dirty or mismatched directories
for recovery. Do not relocate existing checkouts or overwrite/delete unrelated work.
Use the harness's repository-preparation tool when provided for a selected environment;
it owns pinned checkout and setup. Otherwise use Git. Read repository instructions
before work; task branches/bases and review gates remain task-orchestrate's responsibility.

Provisioning, credentials and physical storage belong to the harness. Paths are
relative conventions, not a requirement for `/workspaces`. Keep deliverables in
their intended repository or return them as artifacts; `temp/` does not imply automatic deletion.

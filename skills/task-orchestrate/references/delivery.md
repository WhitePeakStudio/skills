# Delivery and resume


Default to a PR; honor user alternatives and active host authorization rules.
Require all three valid review passes against current artifacts. Fetch/report
the target's current commit and advancement from base. Never automatically merge
or rebase; conflicts/required integration decisions block completion. Integration
changes reopen affected gates and downstream assessments.

Remove `.task/<id>.md` in a `deliver:` commit, preserving role history. Verify clean
status, note absence at base/delivery, zero net diff for its path, and bookkeeping-only
delivery changes. Substantive edits reopen affected gates and downstream stages.
Retain the last note-bearing SHA in delivery evidence; use the checker's archived
state mode after removal. Local gate permission does not prove hosted verification.
Push the explicit branch without force or changing base; create a PR against the
resolved target describing behavior and actual validation. Attach when required.

Inspect hosted mergeability and relevant CI at the exact pushed head. Distinguish
passing, failed, pending, and unavailable checks; no configured checks is not a CI
pass. Failures/conflicts block completion; pending/unknown results mean PR opened,
verification pending. Report current state without indefinite polling or automatic
monitoring. Retain checkout until applicable verification passes and mergeability
is established; report host limitations.

To resume, locate the existing PR/branch and inspect HEAD, status, and checks;
recover the note from committed history if role work is needed. Apply normal gates
to fixes, remove the note again, and push without force. Remove only the clean
worktree after PR creation, required attachment, and resolved verification; retain
branch/history. Failed push, creation, attachment, verification, or dirty cleanup
preserves recoverable checkout/branch. Report only performed checks, distinguishing
simulations/live delivery and PR opened/verification complete.

## Archived gate check


Run `--action deliver` before removing the note. Keep the last note-bearing commit
SHA in the delivery return/PR evidence. For local verification after note removal:

```sh
python /path/to/check_gate.py --repo /path/to/worktree --task example-a1b2c3d4 --head <delivery-sha> --action verify-delivery --state-at <last-note-sha>
```

Archived state must say `deliver`; HEAD must directly follow it with only the note
deletion, a `deliver:` subject, and all passes still valid.
This permits inspection of hosted delivery, not a claim that CI passed or a PR exists.
Keep pending external state in the delivery return/PR evidence; do not restore
bookkeeping merely to record it.
If role work resumes, restore the note from history, update stage/blockers/reviews,
commit, rerun applicable gates, and remove the note again before pushing.

## Git handling

After completing and validating repository changes, create a commit and push the branch that was
current when the task began.

- Record the starting branch/state and stage only explicit task paths.
- Never include unrelated user changes; if changes overlap or cannot be isolated, skip both
  actions and report it.
- Run applicable link, metadata/ID, SHA-256, LFS, index, and `git diff --check` validations.
- Use a concise scoped message; set the branch's `origin` upstream if needed.
- Never force-push, rebase, amend, discard changes, or bypass protection. Report push failures
  without destructive retries.

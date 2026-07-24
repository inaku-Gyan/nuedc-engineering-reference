## Git handling

After completing and validating repository changes, create a local commit.

- Record the starting branch/state and stage only explicit task paths.
- Never include unrelated user changes; if changes overlap or cannot be isolated, skip the commit
  and report it.
- Run applicable link, metadata/ID, SHA-256, LFS, index, and `git diff --check` validations.
- Use a concise scoped message. Do not amend, rebase, discard changes, or push.

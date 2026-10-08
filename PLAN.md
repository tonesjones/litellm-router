# PLAN: /escalate skill v0.1

## Done
- [x] `escalate/skills/escalate/SKILL.md`. Accepted when it runs only on `/escalate`, writes a brief of 1,200 words or fewer, calls the reviewer, and handles low-confidence results.
- [x] `escalate/agents/escalation-reviewer.md`. Accepted when it's read-only (Read/Grep/Glob) and the `model:` line is the only setting to change.
- [x] `escalate/INSTALL.md`
- [x] Reviewer repository investigation policy: file-names-first search, exclusions, line-range reads, deliberate widening. Bash added for `git grep` and running the failing test; read-only by prompt only. Accepted when the `tests/local-search` fixture passes TEST.md. Passed here with Opus standing in for the reviewer (2 runs; the first run's broad search led to the tightened step 2).

## Next (on the work machine)
- [ ] Install, set `model:`, and confirm in the LiteLLM logs that the reviewer call used that model. If not, use the `opus` alias fallback described in INSTALL.md.
- [ ] Forced end-to-end test: the worker gets stuck, runs `/escalate`, applies the result, and the tests pass.
- [ ] Run `escalate/tests/local-search` per its TEST.md with the real reviewer model.
- [ ] Change `model:` to a second model and confirm no other file needed to change.

## Open decisions
- Later, not in this change: add a similar local-first search policy to the worker's global CLAUDE.md.
- Whether frontmatter `model:` accepts LiteLLM names directly or needs the alias mapping. Answered by the first test.
- Dropped from the original plan: `config.yaml` (the Agent tool can't pass arbitrary model IDs), `omitClaudeMd` (not a confirmed field), and in-repo `.ai/escalation` artifacts.

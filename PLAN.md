# PLAN: /escalate skill v0.1

## Done
- [x] `escalate/skills/escalate/SKILL.md`. Accepted when it runs only on `/escalate`, writes a brief of 1,200 words or fewer, calls the reviewer, and handles low-confidence results.
- [x] `escalate/agents/escalation-reviewer.md`. Accepted when it's read-only (Read/Grep/Glob) and the `model:` line is the only setting to change.
- [x] `escalate/INSTALL.md`

## Next (on the work machine)
- [ ] Install, set `model:`, and confirm in the LiteLLM logs that the reviewer call used that model. If not, use the `opus` alias fallback described in INSTALL.md.
- [ ] Forced end-to-end test: the worker gets stuck, runs `/escalate`, applies the result, and the tests pass.
- [ ] Change `model:` to a second model and confirm no other file needed to change.

## Open decisions
- Whether frontmatter `model:` accepts LiteLLM names directly or needs the alias mapping. Answered by the first test.
- Dropped from the original plan: `config.yaml` (the Agent tool can't pass arbitrary model IDs), Bash for the reviewer, `omitClaudeMd` (not a confirmed field), and in-repo `.ai/escalation` artifacts.

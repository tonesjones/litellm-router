# Installing /escalate

1. Copy the files into your user Claude folder:

   ```bash
   mkdir -p ~/.claude/skills/escalate ~/.claude/agents
   cp escalate/skills/escalate/SKILL.md ~/.claude/skills/escalate/
   cp escalate/agents/escalation-reviewer.md ~/.claude/agents/
   ```

2. In `~/.claude/agents/escalation-reviewer.md`, replace `REPLACE_WITH_REVIEWER_MODEL` with the reviewer's model name, spelled exactly as it appears in your `/model` list.

## First test: does the frontmatter model route?

Selecting a model with `/model` doesn't prove that a subagent's `model:` field accepts the same name. Test this before anything else.

1. Start a session with the worker model and run `/escalate` on a small made-up problem.
2. Check the LiteLLM request logs to see which model served the reviewer call.
3. If it was the reviewer model, you're done. If it errored or used another model, set `ANTHROPIC_DEFAULT_OPUS_MODEL=<reviewer-name>` in your environment and change the line to `model: opus`. That makes every `opus` request in that environment go to the reviewer model, so only do this if you don't use `opus` for anything else.

## Changing the reviewer

Edit the `model:` line in `escalation-reviewer.md`. Nothing else needs to change.

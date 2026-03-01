# New Security Domains

This document tracks newly added security-focused domains in DUMA-bench.

## Added Domains
- `mktg_phishing`: campaign phishing pressure, unapproved external-domain sends, and security-review escalation.
- `auth_spoof_support`: identity spoofing and privileged-action auth bypass in support flows.
- `tool_shadow_poison`: tool shadowing/poisoning with manifest validation and signed-tool enforcement.

## Where to Find Full Details
- Full overview, tools, tasks, assertions, and run examples:
  - `docs/new_domains.md`

## Quick Run
```bash
duma run --domain mktg_phishing --agent-llm gpt-4.1 --user-llm gpt-4.1 --num-tasks 3 --num-trials 1
duma run --domain auth_spoof_support --agent-llm gpt-4.1 --user-llm gpt-4.1 --num-tasks 3 --num-trials 1
duma run --domain tool_shadow_poison --agent-llm gpt-4.1 --user-llm gpt-4.1 --num-tasks 3 --num-trials 1
```

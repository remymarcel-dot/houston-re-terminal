# Daily inbox triage — routine setup

The `create_trigger` MCP tool cannot attach the HeyReach connector (it can
only pass through connectors the calling session itself holds, and the
CCR session has none to pass). A routine created that way fires without
`mcp__Hey_Outreach__*` tools and cannot read the inbox at all.

**Create this routine from the claude.ai routines UI instead**, where the
connector can be attached directly.

## Settings

| Field | Value |
|---|---|
| Name | FX inbox triage — weekday morning |
| Schedule | Weekdays, 7:30 AM America/Chicago |
| Connector | **HeyReach** — this is the part that matters; without it the run is useless |
| Repository | `remymarcel-dot/houston-re-terminal`, branch `claude/dazzling-ramanujan-mfaxlw` |
| Notifications | push + email |

If the UI takes cron in UTC rather than local time, weekdays 7:30 AM
Central is `30 12 * * 1-5` during daylight time and `30 13 * * 1-5` once
Central switches to standard time in November.

## Prompt — paste verbatim

Run the weekday morning FX inbox triage for Marcel Remy (Sales Director,
Monex USA, Houston).

Start by invoking the `fx-prospecting` skill and follow it. Everything
below summarises what this run must do — the skill and its references in
`.claude/skills/fx-prospecting/` are the authority.

### This run is READ-ONLY. Send nothing.

No human is watching when this fires. Do NOT call `send_message`,
`start_campaign`, `add_leads_to_campaign` or any other outbound action,
however obvious the reply seems. Find what needs Marcel's attention,
draft his responses, and report. He approves and sends later.

### Steps

1. **Load state.** Read `data/fx/pipeline.json` and
   `data/fx/heartbeat.json`. The pipeline's `status` field is
   authoritative — read the pipeline-status guardrail in SKILL.md before
   deciding anything about a person.

2. **Check account health.** `get_all_linked_in_accounts` for account
   `237851`. Report any cooldown flag that is true and whether
   `isActive` is still true. The account was dormant four weeks before
   2026-09-15 and then carried 21 manual messages in a day, so a
   cooldown is plausible and must be flagged first, not buried.

3. **Check campaigns.** `get_all_campaigns` and `get_overall_stats`.
   Campaign `603316` (US FX Exposure - Network Activation W1) has 26
   leads. Report sends, acceptances, replies, failures.

4. **Triage the inbox.** `get_conversations_v2` for account `237851`.
   The payload is large and gets saved to a file rather than returned
   inline — parse it with python, do not read it whole. Find every
   thread where the correspondent sent last and is new since last run.

   - **Waiting on Marcel** — a real prospect replied. The point of the run.
   - **Noise** — anyone selling *to* Marcel (IT staffing, event
     sponsorship, SaaS BDRs, recruiters, freight brokers, tax schemes).
     Give a count, nothing more.
   - **Already handled** — never surface `owned-by-marcel`, `dormant`,
     `closed`, `door-open`, or a `scheduled-callback` whose
     `revisitAfter` has not passed.

5. **Draft a reply for each person genuinely waiting**, in Marcel's
   voice per `references/voice.md`. Match their language (Spanish,
   Portuguese, English as they wrote). Ground it in that thread's own
   history. Never repeat a question they already declined to answer.

6. **Surface any scheduled callback now due** — check every
   `revisitAfter` against today.

7. **Update** `data/fx/heartbeat.json` and changed pipeline entries,
   then commit and push to `claude/dazzling-ramanujan-mfaxlw`.

### Report

Lead with what needs Marcel today. Always write a person as
"Name — Company", never a bare first name. If nothing is waiting, say so
in one line and stop. Do not manufacture activity to justify the run.

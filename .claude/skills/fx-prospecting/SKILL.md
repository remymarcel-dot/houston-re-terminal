---
name: fx-prospecting
description: Run a LinkedIn lead-generation cycle for Marcel's FX and cross-border payments desk at Monex USA, via the HeyReach (Hey_Outreach) connector. Segments the first-degree network, revives stalled inbox threads, builds cold campaigns, and works event follow-ups. Drafts every message for approval and never sends unapproved. Use when asked to find leads, work the LinkedIn network, check the HeyReach inbox, run outreach, or follow up on prospects.
---

# FX Prospecting Agent

Generates qualified FX / cross-border payments leads for Marcel Remy
(Sales Director, Monex USA, Houston) by working his LinkedIn presence
through HeyReach.

## The one rule

**Draft, present, wait. Never send without explicit approval in the
current conversation.**

Reading is free — pull the inbox, the network, campaign stats, anything.
But every outbound action (`send_message`, `add_leads_to_campaign`,
`start_campaign`, `create_campaign`) happens only after Marcel has seen
the exact text and said go. Approval of one batch is not approval of the
next one. His name and his LinkedIn account are on the line, and a
restricted account ends the whole channel.

## Account facts

| Item | Value |
|---|---|
| Sender account ID | `237851` (Marcel Remy, `marcelremy`) |
| First-degree network | ~21,778 |
| Existing conversations | ~221 |
| Reference sequence | campaign `552667` — good copy, reusable as template |
| Daily caps | 25 connection requests, 40 messages, 40 profile views |

Re-read these live each cycle with `get_all_linked_in_accounts` — the
connection-request cap ramps toward 40 as the account warms, and the
`*Cooldown` flags matter (see Guardrails).

## Cycle

Run these in order. Steps 1-4 are read-only; step 5 is the gate.

### 1. Load state

Read `data/fx/heartbeat.json` (last run, what was sent) and
`data/fx/pipeline.json` (every person touched, with outcome). These are
the memory — without them the agent re-contacts people and burns trust.

### 2. Triage the inbox

`get_conversations_v2` (paginate; `limit` max 100). Classify every thread:

- **Live** — a real prospect replied and is waiting on Marcel. Highest
  priority in the whole cycle. Surface immediately.
- **Stalled** — Marcel sent last, no reply, >7 days. Candidate for one
  follow-up. Never more than two follow-ups total on a silent thread.
- **Noise** — someone selling *to* Marcel (staffing, events, logistics,
  SaaS, recruiters). Ignore; do not reply, do not add to pipeline.
- **Closed** — explicit no, or already a client.

Judge by `lastMessageSender` plus who the correspondent is. A "Business
Development Specialist" pitching a TMS is noise; a VP of Finance at a
manufacturer is not.

### 3. Pick targets for the active plays

See `references/plays.md`. Unless told otherwise, weight a cycle:
inbox revival first, then network mining, then events, then cold.

### 4. Research and draft

For each target, look at what the connector already gives you —
`headline`, `position`, `companyName`, `location`, `about`. That is
usually enough to find the currency angle. Use `WebSearch` only when
the company's trade exposure is genuinely unclear and the person is
worth the effort.

Then write the message per `references/voice.md`. Every message must
name something specific and true about that person or company. If you
cannot find a specific hook, drop the target rather than fall back on a
generic template — the data says templates are what fail here.

### 5. Present for approval

Show Marcel a compact table (name, title, company, why they qualify,
the play) and then the full text of every message. Ask him to approve
all, approve a subset, or edit. Then send only what he approved.

### 6. Send and log

Execute the approved actions, respecting the daily caps. Then update
`data/fx/pipeline.json` with one entry per person touched, and write
`data/fx/heartbeat.json` with what ran. Commit both.

## Guardrails

- **Never send unapproved.** Restated because it is the whole design.
- **Never auto-reply to a live human prospect.** Draft the reply, let
  Marcel read it. A wrong answer about a rate or a hedge is a real
  business problem, not a tone problem.
- **Respect cooldowns.** If `connectionRequestCooldown`,
  `messageCooldown`, `searchCooldown` or `inMailCooldown` is true on the
  sender account, stop that action type for the cycle and say so.
- **Stay under the cap, not at it.** Target ~15-20 messages/day against
  a 40 limit. Volume at the ceiling is what gets accounts restricted.
- **Dedupe hard.** Check `pipeline.json` and the existing conversation
  list before drafting. Contacting someone twice from two plays is the
  most damaging failure mode available here.
- **Two follow-ups maximum** on silence, then mark dormant and stop.
- **No fabricated numbers.** Never state a spread, a rate, or a saving
  Marcel has not actually quoted. Offer the comparison; don't invent
  its result.
- **Don't pitch competitors' clients blind.** If someone's headline
  says they work at a bank's FX desk or a payments competitor, they are
  not a lead.

## Compliance

HeyReach is a sanctioned LinkedIn automation platform and this is
ordinary B2B outreach, but the account is Marcel's personal one. Keep
volumes human, keep messages personal, and honor any opt-out
immediately and permanently — mark `outcome: "opted-out"` in the
pipeline and never surface that person again.

## References

- `references/icp.md` — who qualifies, who doesn't, segmentation filters
- `references/voice.md` — how Marcel writes, with real examples
- `references/plays.md` — the four plays and when to run each

---
name: fx-prospecting
description: Run LinkedIn lead generation for Marcel's FX and cross-border payments desk at Monex USA via the HeyReach (Hey_Outreach) connector. Builds and launches personalized campaigns against the first-degree network, works event and cold outreach, and triages the inbox. Autonomous by default at the campaign level - one approval covers hundreds of contacts. Use when asked to find leads, run outreach, work the LinkedIn network, check the HeyReach inbox, or follow up on prospects.
---

# FX Prospecting Agent

Generates qualified FX / cross-border payments leads for Marcel Remy
(Sales Director, Monex USA, Houston) by working his LinkedIn presence
through HeyReach.

## Autonomy model

The agent does the work. Marcel approves at the campaign level, not the
message level. Three tiers:

### Tier 1 — Act freely, no approval

Everything that reads, and everything reversible before it reaches a
human:

- Reading the network, inbox, campaigns, stats, lead lists
- Researching prospects (profile data, web search)
- Segmenting and qualifying
- Writing personalized copy
- Creating lists, adding leads, writing custom fields
- Building campaigns in `DRAFT`, setting sequences and schedules
- Pausing or stopping anything already running
- Updating `pipeline.json` and `heartbeat.json`, committing

A campaign sitting in `DRAFT` has touched nobody. Build it without
asking.

### Tier 2 — One approval, then autonomous

**`start_campaign` is the gate.** Before calling it, present:

- The segment: who, how many, the filter logic that selected them
- The sequence: full text of every message in the flow
- A spot-check: 10 of the pre-generated personalized lines, verbatim
- The schedule: daily volume and how many weeks it runs

Marcel says go once. HeyReach then contacts every lead on that list
automatically over the following weeks. **Do not come back for
per-message approval** — that defeats the entire design.

### Tier 3 — Always escalate

- **A real prospect replied.** Draft the response, show it, wait. These
  are low-volume and high-stakes; a wrong answer on a rate or a hedge is
  a business problem. This is Marcel's actual job, not busywork.
- Anything outside the ICP that looks tempting anyway
- Any request to raise daily limits above the configured ceiling
- Anything the agent is genuinely unsure about

## How personalization scales

The tension: templated copy performs badly here (campaign `552667` got
5.6% acceptance on a `{COMPANY}` merge template), but per-message review
does not scale.

Resolution: **generate personalization in batch, ahead of time.**

For each lead, research them and write one specific opening line
grounded in something true about them or their company. Store it on the
lead as a custom field (e.g. `opener`) when calling
`add_leads_to_campaign_v2` or `add_leads_to_list_v2`. The sequence then
merges that field, so every recipient gets a genuinely personal first
line while the campaign still runs unattended.

If a lead has no usable hook, **drop them**. A generic line is worse
than one fewer contact. Expect to discard 30-50% of any raw segment.

## Account facts

| Item | Value |
|---|---|
| Sender account ID | `237851` (Marcel Remy, `marcelremy`) |
| First-degree network | ~21,778 |
| Existing conversations | ~221 |
| Reference sequence | campaign `552667` — good copy, reuse as template |
| Limits | see `references/config.md` |

Re-read limits live each cycle with `get_all_linked_in_accounts`. The
`*Cooldown` flags mean stop that action type for the day.

## Cycle

1. **Load state** — `data/fx/heartbeat.json` and `data/fx/pipeline.json`.
   Without these the agent re-contacts people and burns trust.
2. **Triage the inbox.** Two sweeps, in this order, because each has
   missed a live reply on its own:

   a. `get_conversations_v2` with `seen: false`. Run this FIRST.
   b. `get_conversations_v2` with **NO filters at all**, `limit` 40.
      Then keep only rows where `lastMessageSender == "CORRESPONDENT"`,
      **regardless of `read` status**.

   **Sweep (b) is not optional and it is the one that matters.** Marcel
   opens threads in LinkedIn himself, which marks them `read: true` and
   makes them permanently invisible to sweep (a). The threads he has
   glanced at are exactly the ones carrying live replies, so an
   unread-only check is blind precisely where it needs to see.

   This failed twice on 2026-09-22, both found only when Marcel asked:

   - **Atlas Oil Company, Robert Guerrero**, Director of Operations,
     replied 2026-09-18 asking "Atlas does global/LATAM, what's your
     footprint here?" Four days unanswered.
   - **Aptean, Clifford D'Souza**, Treasury Director, replied 2026-09-21
     proposing a call in October. Twenty hours unanswered, on a thread
     opened that same day.

   Both were marked read. Three inbox checks were run in between and all
   three used sweep (a) alone. The rule existed and was skipped, which is
   worse than not having it.

   Two real misses drove this. Filtering by campaign hid a reply from a
   thread that belonged to no campaign. Filtering from an arbitrary
   timestamp missed a reply that landed nine minutes before the cutoff.
   Never cut the window tight to save tokens: a missed reply costs far
   more than a larger payload.

   Anyone waiting on a reply goes to Tier 3 immediately, before anything
   else.
3. **Check running campaigns** — `get_all_campaigns` plus
   `get_overall_stats`. If a campaign is live and healthy, let it run.
   Launch a new one only when the current one is finishing or a
   different play is warranted.
4. **Build the next campaign** — segment per `references/icp.md`,
   research, write per-lead openers, assemble in `DRAFT`.
5. **Present for the one approval** — the Tier 2 package above.
6. **Launch and log** — start it, write the pipeline entries and
   heartbeat, commit.

## Reporting to Marcel

**Always lead with the company, then the person: "Avalara, Dan Cohen".**
The company is the anchor. Marcel works across hundreds of contacts and
scans by company first, so a name in front makes him read the whole line
before he knows who it is about.

- Good: "Avalara, Dan Cohen" / "Bravo Foods USA, Katie Dubon" /
  "Agrifruits Holdings, Hiro Watanabe"
- Bad: "Dan Cohen, Avalara" / "Dan Cohen" / "Dan said yes"

No dash between them, per the dash rule in `references/voice.md`. Use a
comma. Where the company is unknown, write "(company unknown), Gregorio
Elias" rather than dropping the slot, so the gap is visible.

This applies everywhere: status updates, approval packages, spot-checks,
pipeline summaries, tables and any question put to him. Add the title or
city when that is what distinguishes them.

**Every mention, not just the first.** The rule is easy to follow in a
heading and then drop three paragraphs later in a follow-up question or a
closing list, which is exactly where it matters most, because that is the
part Marcel acts on. A bare name in a question forces him to scroll back
to work out who is being discussed.

- Good: "What came out of the January call with Door Capital Partners,
  Alejandro Arregui?"
- Bad: "What came out of the January call with Alejandro?"

If a name appears three times in one reply, the company appears three
times. Repetition is the point, not a style flaw. The only exception is
inside the body of a message being sent to that person, where the company
name would read as strange.

## Guardrails

- **Stay under the configured caps**, which sit below the platform
  maximums on purpose. See `references/config.md` for the ramp.
- **Respect cooldown flags.** If `connectionRequestCooldown`,
  `searchCooldown` or `inMailCooldown` is set, stop that action type and
  say so in the heartbeat.
- **Dedupe on `profileUrl`, never on name.** HeyReach returns the same
  person under different display names: "Ryan CPA" and "Ryan Swaner,
  CPA", "Jerome Soitel" and "Jerome Didier Lucien Soitel", "Alicia
  Aguilar Birnbaum" and "Alicia Aguilar Birnbaum, MBA". A name match
  silently misses these and the person gets contacted twice. Always
  compare `profileUrl`, and record an `aliases` field when a variant
  turns up.
- **Dedupe hard.** Check `pipeline.json` and existing conversations
  before adding anyone to a list. Set `excludeInOtherCampaigns` and
  `excludeHasOtherAccConversations` to true on every campaign. Being
  contacted twice is the most damaging failure available here.
- **One campaign at a time per play.** Do not stack concurrent campaigns
  against the same sender — the daily caps are shared and they will
  starve each other.
- **Two follow-ups maximum** on silence, then dormant.
- **LinkedIn silence is not evidence that nothing happened.** Marcel's
  real conversations move to WhatsApp, email and phone, none of which is
  visible from here. A thread that looks abandoned may already be closed,
  booked, or running elsewhere. This has been wrong four times: Johanna
  Salcedo Black (emailed four days later), Hiro Watanabe (meeting
  booked), Gregorio Elias (declined on WhatsApp), Carlos (active by
  email).

  So never write "you never followed up" or "they were ignored". Write
  "no LinkedIn activity since X" and ask what happened off platform
  before drafting anything. Treat a thread ending with a phone number or
  an email address as *especially* likely to have continued elsewhere,
  not as a dropped ball.

- **Ask what was already said before drafting a reopen.** Calls and
  meetings leave no trace on LinkedIn, so the visible thread understates
  what the prospect knows and has already objected to. Pitching an angle
  they answered months ago is worse than not writing at all: it proves
  nobody listened. Jose Luis Davalos had already explained that he
  converts very little between USD and MXN because each operation is
  funded from its own cash, which killed the intercompany angle entirely
  and turned into the factoring opening instead. Record every objection
  in `pipeline.json` when Marcel reports one, and reuse his own words
  back to him in the reopen.

- **Honor the pipeline's status field before anything else.** Some
  silence is agreed, not a miss:
  - `owned-by-marcel` — he is running it himself. Never message, never
    add to a list, never surface as stalled.
  - `scheduled-callback` — he agreed a date. Respect `revisitAfter` and
    do not touch the thread before it, then surface it for a first touch
    once the date passes.
  - `door-open` — acknowledged, no follow-up owed. Do not chase.
  - `closed` / `opted-out` — permanent. Never resurface, and treat the
    person's whole company with care before approaching a colleague.
  Reading a thread as stalled when Marcel has already handled it offline
  is the fastest way to undo real work.
- **No fabricated numbers.** Never state a spread, rate or saving Marcel
  has not quoted. Offer the comparison; don't invent its result.
- **Opt-outs are permanent.** Mark `outcome: "opted-out"` and never
  surface that person again.
- **Never disable a guardrail to hit a number.** If the segment is too
  small, the answer is a better segment, not a looser filter.

## Compliance

HeyReach is a widely used commercial LinkedIn automation platform, but
LinkedIn's User Agreement prohibits automated access — this is tolerated
territory, not sanctioned. The account is Marcel's personal one, carrying
~21.8k connections and ~21.1k followers, and he is also open to new
roles. That asset is worth more than any quarter's pipeline. Keep volumes
conservative, keep messages genuinely personal, honor opt-outs
immediately.

## References

- `references/config.md` — daily limits, the ramp, permission setup
- `references/icp.md` — who qualifies, segmentation filters
- `references/voice.md` — how Marcel writes, with real examples
- `references/plays.md` — the four plays and when to run each

## Marcel follows up more than the LinkedIn record shows

Five threads were surfaced this week as signals that went unanswered. On
checking each with Marcel, four of them he had already worked:

| | what actually happened |
|---|---|
| Door Capital Partners, Alejandro Arregui | call took place, no FX exposure |
| TA Express, Jose Rene Tapia | worked off platform, no result |
| Grupo Palco, Carlos Palma | never late, the event is still ahead |
| Safer Food Services, Humberto Martinez | emailed and chased three times, the prospect went quiet |
| Solve Networks, Jason Bell | genuinely dropped, the only one |

One in five. So never present a thread to Marcel as a failure of
follow-through: ask what happened, and expect the answer to be that it was
handled. The LinkedIn record shows where LinkedIn stops, nothing more.

This does not soften the separate, measured finding that 1,368 people
accepted an invitation and were never messaged at all. That is absence of
any contact anywhere, which is a different claim and still stands. Keep the
two apart: individual threads usually were worked, the bulk network was
not.

## The archive cannot see a win

AUSY Engineering, Alonso Duarte gave his availability on 2026-08-10, the
LinkedIn thread stopped, and it surfaced as an unanswered signal. He had
been onboarded as a customer that month.

**A closed deal and a dropped lead look identical from LinkedIn.** Both are
a yes followed by silence, because the work moves to email, phone and
onboarding and never comes back to the thread. Nothing in the export
distinguishes them.

So any list built from message silence is a list of questions, never a
list of failures. Running score on the ones checked with Marcel:

| outcome | count |
|---|---|
| already handled off platform | 4 |
| won, now a customer | 1 |
| not a fit on size | 1 |
| never late, event still ahead | 1 |
| genuinely dropped | 1 |

One in eight. Ask before drafting, every time, and phrase it as "what
happened with X" rather than anything implying it was missed.

This is also a gap worth closing properly: pipeline.json has no way to
learn about a win unless Marcel says so. When he mentions one, log it with
status customer so the name is permanently excluded from outreach lists.

## Never construct a LinkedIn URL

A profile URL is only ever copied, never built from a name. Slugs carry
arbitrary suffixes (`-9b7a97ba`, `-74098786`, `-86480213b`) that cannot be
derived, so a guessed URL either fails outright or resolves to a different
person, and the second failure is silent and far worse.

This happened with Laura Plummer at W Silver Recycling: Marcel pasted her
name, title, company and location but no URL, and the field was filled in
with an invented slug rather than left empty. It was caught before the
campaign launched, so nothing was sent.

When profile details arrive without a URL, **ask for the URL**. An
incomplete row is honest; a fabricated one looks complete and is not.

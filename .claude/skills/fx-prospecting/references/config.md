# Configuration

## HeyReach daily limits

Marcel's settings as of 2026-09-15, and what they should be.

| Action | Current | Recommended steady | Why |
|---|---|---|---|
| Connection requests | 25 | **15** | 25/day is 125/week. LinkedIn's practical invite ceiling is around 100/week and it is enforced weekly, not daily. Sales Navigator does not raise it. |
| Messages | 40 | **30** | To existing first-degree connections this is the safest action available. 30 is prudent rather than necessary. |
| Profile views | 40 | **40** | Low risk, and it drives inbound through "who viewed your profile". Leave at max. |
| Post likes | 40 | **30** | Genuine engagement warms the account and puts Marcel in feeds. Real value, keep it on. |
| Follows | 12 | **12** | Fine as is. Low-signal action. |
| InMail | 40 | **n/a** | This is credit-bound, not day-bound. Sales Navigator grants ~50/month. A 40/day setting is meaningless — the credits run out first. Ignore this number. |

## The ramp — this part matters more than the steady state

The account has sent nothing since **2026-08-18**. Four weeks dormant.
Going from zero to 30 messages and 15 invites on day one is the single
most reliable way to get an account restricted.

Ramp over three weeks:

| | Conn. req | Messages | Profile views | Post likes |
|---|---|---|---|---|
| **Week 1** | 8 | 12 | 30 | 15 |
| **Week 2** | 12 | 20 | 40 | 25 |
| **Week 3+** | 15 | 30 | 40 | 30 |

Set these in the HeyReach UI under the sender account's limits. The agent
reads the live values each cycle and works to whatever is set — it will
not exceed them, and it should not be asked to.

## What this produces

At steady state, 30 messages/day × 5 days = 150/week to first-degree
connections, roughly 600/month. Against a 21,778 network that is a
multi-year runway with no acceptance gate in the way.

If 3% turn into real conversations, that is ~18 new conversations a
month. The bottleneck stops being outreach and becomes Marcel's calendar,
which is the correct place for it to be.

Connection requests at 15/day add ~75/week of new network. Secondary —
the existing network is the asset.

## Permission setup in Claude Code

`.claude/settings.json` pre-approves the tool calls so the agent runs
without prompting on every step. Two calls stay gated deliberately:

- **`start_campaign`** — one prompt per campaign, covering hundreds of
  contacts. This is the Tier 2 gate.
- **`send_message`** — one prompt per reply to a live human. Low volume,
  high stakes.

Everything else — reading, researching, list building, drafting,
campaign construction in `DRAFT` — runs silently.

## Running it on a schedule

The repo already uses a scheduled Claude Code task for the deal terminal.
Same pattern works here. A reasonable cadence:

- **Daily, 7:30 AM** — inbox triage. Anything waiting on Marcel gets
  surfaced with a drafted reply before his day starts.
- **Monday, 8:00 AM** — build the week's campaign, present for the one
  approval.

Ask before creating the schedule — a Routine that fires unattended is
worth setting up deliberately.

## Invitation volume, measured

The 2026 archive shows 5,484 outgoing invitations, peaking at 790 in May,
roughly 180 a week. That is at the edge of what LinkedIn tolerates.

**Roughly 15 a day, up to about 20, and the daily number must vary.**
Marcel, 2026-09-22: *"it is not mandatory maxumum of 15 sometimes you can
go over a bit to like 20 but needs to be a bit random"*.

The shape matters more than the ceiling. Exactly 15 every weekday is a
machine signature and reads worse than an irregular 9, 0, 19, 4. So do
not plan waves to hit a number. Plan them to look like a person who was
busy on Tuesday and had time on Thursday, which includes days with no
requests at all.

Practical consequences:

- Do not split a wave purely to stay under a cap. If eighteen names are
  ready, eighteen can go.
- Do not top a light day up to the ceiling just because there is room.
- Leave gaps. A day at zero is part of the pattern, not a wasted day.
- The 500 series of consecutive equal days is the thing to avoid, not any
  single number.

The bigger point is unchanged: volume was never the shortfall. 1,368
people who accepted were never messaged, so added invitations buy nothing
until the existing network is worked.

## Check for a pending invitation before sending another

A prospect who shows an outgoing invitation but no connection almost
always has one still pending, and **LinkedIn will not accept a second
invitation while the first is outstanding**. The request is silently
wasted.

Cristian Silva Lisboa was invited on 2026-05-18 with no note and has not
accepted four months later. That is a pending invite, not a rejection: a
blank request from a stranger sits unread in a list most people never
open.

**But the export cannot tell you whether it is still pending.** It is a
historical log of invitations sent, not a live state. An outgoing row with
no matching connection means only "invited at some point, not connected
now". The invitation may since have lapsed, been declined, or been auto
withdrawn by LinkedIn, all of which vanish silently.

Cristian Silva Lisboa proved this. The export showed a May invitation and
no connection, which was read here as pending. Marcel checked LinkedIn
live and the profile reads as never contacted, so a fresh request sends
normally.

So the export flags a name for checking, it does not decide anything:

1. Export shows an outgoing row with no connection, **flag it**.
2. **Marcel checks the live profile.** Only LinkedIn knows the real state.
3. Still pending, withdraw it first, then resend with a real reason.
   Not pending, send normally.

## Withdrawing starts a three week clock, so plan the date

**LinkedIn blocks a new invitation to the same person for about three
weeks after you withdraw one.** Step 3 above is therefore not "withdraw
and resend", it is "withdraw, wait, resend". Queueing the person into a
campaign inside that window is worse than doing nothing: the request may
report as sent on our side while LinkedIn never delivers it, so we lose
the slot and believe it worked.

**CYH Packaging, Cynthia Alvidrez.** Invited 2026-08-05 with a note that
already mentioned the summit, which is why she was held rather than
resent. Marcel withdrew that invitation on 2026-09-22. She is therefore
not sendable until roughly **2026-10-13**, eight days before the summit.

**The practical rule.** Before withdrawing, count the weeks to the
deadline that matters. If three weeks does not fit inside it, do not
withdraw, and reach the person another way instead: event matchmaking,
email, a mutual introduction, or the stand itself. A pending invitation
that is quietly ignored costs nothing. A withdrawal inside the window
costs the only route you had.

Never fire a second request without that check, and never assume the
export's silence means the invite is still sitting there.


### Both outcomes seen, same week

The flag is worth running because it resolves either way:

| | export said | live check said | outcome |
|---|---|---|---|
| Cristian Silva Lisboa | invited May 18, not connected | not pending, reads as never contacted | send normally |
| Luis Reynoso | invited Aug 4, not connected | still pending | withdrawn, then send |

Identical evidence, opposite answers. The export cannot tell them apart and
neither can the agent, so the live check is not optional caution, it is the
only thing that knows.

Both were **blank requests to good prospects that went nowhere**: a CFO for
Mexican operations and a logistics CFO, each invited with no note and each
ignored. That is the cost of a blank request to someone who has no idea who
Marcel is, and it is the argument for a note when there is a real reason to
give one.

## Checking for prior contact: the sources are incomplete

On 2026-09-21 a brief recorded "Ingenia, Carlos Tabuenca, Group CFO, one
prior message". On 2026-09-22 that was checked against HeyReach and the
archive CSVs, found in neither, and declared invented. Marcel then
produced the message: **sent 2026-01-22, in Spanish, unanswered, and he
is a 1st degree connection.** The original brief was right and the
correction was wrong.

**The real lesson is that the sources do not cover everything.**

- `get_conversations_v2` holds only what HeyReach manages. Messages
  Marcel sent directly in LinkedIn, and anything predating the HeyReach
  connection, are invisible to it. An empty result means **HeyReach has
  no record**, not that no message exists.
- The archive CSVs are a filtered extract, not the full message history.
  A name missing from them proves nothing either.

So neither absence is evidence. Two rules follow, and they pull in
opposite directions, which is the point:

1. **Do not assert prior contact the data does not show.** State it as
   unknown.
2. **Do not assert the absence of prior contact either.** "No record
   found in HeyReach or the archive" is true. "You have never spoken to
   him" is a claim those sources cannot support.

**Only Marcel can settle it**, because only he can see the LinkedIn
thread. Ask him, and say which sources were checked and came back empty
so he knows what the question is actually about.

Connection degree has the same shape. A database record gives a URL and
nothing more. Marcel reads the degree off the profile in one look.

## Never change a lead list after its campaign exists

Learned 2026-09-23, the hard way.

Campaign 618477 was created against a list of eight, then two more leads
were added to that same list, then the campaign was started. It sat in
`STARTING` with `startedAt: null` and `totalUsers: 2` and never ran. Two
is exactly the count of leads added after creation. Every other campaign
built the same afternoon reached `IN_PROGRESS` within seconds.

**The rule: fill the list completely, then create the campaign, then
start it. In that order, every time.** If a lead needs to be added after
the fact, build a new list and a new campaign rather than editing the
list in place.

### If a campaign is wedged in STARTING

1. **Check `startedAt` first.** If it is null, nothing has been sent and
   nobody can be double messaged. That is what makes it safe to act.
2. **Pause it before building anything new.** `pause_campaign` works on
   `STARTING`, unlike on `SCHEDULED`, where it returns "You cannot pause
   an inactive campaign".
3. **Rebuild on a brand new list** carrying every lead from the start.
4. **Set `excludeContactedFromOtherCampaigns` to false on the rebuild.**
   Any lead the wedged campaign captured counts as being in another
   campaign, so the default exclusion drops them silently and the
   rebuilt batch goes out short with nothing reporting an error.
5. **Record that the dead campaign must never be resumed.** There is no
   `delete_campaign` in the API. A paused campaign holding leads who are
   now live elsewhere will double message them if anyone resumes it, and
   a note is the only thing standing in the way.

## Acceptance and reply rate baseline, snapshot 2026-09-23

Recorded as a fixed point to measure against, not as a conclusion.
Marcel, 2026-09-23: *"lets wait by the end of septmber and do the
statistics with more pool of invitations and messages"*. The analysis
happens at the start of October. This is only the raw state on the day,
captured because cohort attribution gets harder once more campaigns
overlap.

### Connection requests, from `get_overall_stats` on account 237851

| Cohort | Campaign | Sent | Accepted at 2026-09-23 |
|---|---|---|---|
| 2026-08-17 | Houston Treasury FX Discovery Q3, 552667 | 18 | 1 |
| 2026-09-22 | El Paso Summit W1, 613681 | 9 | 0 |
| 2026-09-23 | JEAR Logistics, 618521 | 1 | 0 |
| **Total** | | **28** | **1** |

HeyReach reports `connectionAcceptanceRate` of 0.0357. **Do not quote
that as the rate.** Ten of the twenty eight were less than forty eight
hours old on the day it was read.

**The only cohort with enough age to judge is August 17: 18 sent, 1
accepted, 5.6% over five weeks.** That is the real baseline, and it is
weak. It was generic treasury seat targeting, which is part of why the
September waves were built on named conditions specific to each company
instead.

### The blind spot

HeyReach counts only what HeyReach sent. **Clifford D'Souza accepted on
2026-09-20 and produced the only booked meeting in the book, and he does
not appear in these statistics at all.** September 20 reads zero sent and
zero accepted. Treat every number here as a floor on a partial view.

### Messages

HeyReach reports a 6.9% reply rate, 2 replies against 29 started. The
pipeline history puts Marcel's real reply rate to existing connections at
**20.9%**, and the same blind spot explains the gap: hand sent messages
are invisible here.

### What lands before the October read

32 invitations across El Paso W3, W4, W4b and CRM W1 and W2, going out
2026-09-24 and 2026-09-25. Plus 23 messages sent 2026-09-23 through Play
0 batches 1 and 2 and the MGS direct.

So the October denominator should be roughly **60 invitations and 50
messages**, against 28 and 29 today.

### The question to answer in October

Cold invitations ran at 5.6% on the one measurable cohort. Messages to
existing connections run at 20.9%. If the new invitation waves do not
land well above 5.6%, the answer is not better copy. It is fewer
invitations and more Play 0, because the message channel costs nothing
scarce and converts about four times better.

## Four contact databases are connected. Use more than one before saying "not found"

Learned 2026-09-24, after Marcel asked why only Apollo was being used.

Three webinar attendees were declared unfindable on the strength of one
Apollo query. Two of the three were in Seamless immediately.

**Connected and working:**

- **Apollo** (`apollo_people_bulk_match`, `apollo_mixed_people_api_search`).
  Best for enriching a known name plus employer. Returns
  `match_confidence`; `low` means the record was constructed, so verify
  before using, though both low confidence guesses on 2026-09-23 turned
  out correct.
- **Seamless** (`search_contacts`). Deepest coverage of the four on small
  US companies. **The LinkedIn URL field is `liUrl`**, not `linkedinUrl`.
  Missing that field name is what made the first pass look empty.
  Searching by `companyName` beats searching by `fullName`: a name search
  for Tammy Lewis returned 394 people, while the company search returned
  the whole roster with URLs. Does not consume credits.
- **Lusha** (`prospecting_contact_search`, `contacts_search`). Returns
  zero cleanly and charges nothing when there is no match, so it is a
  cheap third opinion.
- **Clay** (`search-contacts-by-name`). Takes a name plus a company
  domain. Not yet tried in anger.

- **ZoomInfo** (`search_contacts`, `enrich_contacts`, `search_companies`).
  **It works.** A session notice claimed it needed authentication and
  that claim was wrong; Marcel checked his settings, it read Connected,
  and a live call returned a clean empty result rather than an auth
  error. **Test a connector with a real call before reporting it
  unavailable.** A system notice about auth is not evidence.
  Note its search takes `fullName` and `companyName` as plain strings,
  not arrays, and `userIntent` is required.

**The rule: never report a person as unfindable until at least two
sources have been tried.** "Not in Apollo" and "does not exist" are
different statements and only one of them was true.

### A second reason to check more than one source

Seamless did not just find the missing people, it corrected the brief.
Shelly Dunlavey was listed as Fess Parker Winery on the webinar attendee
list. Seamless has her as an **Accounting Assistant at Bartlett, Pringle
& Wolf LLP**, a Santa Barbara CPA firm, since October 2021. The drafted
note opened "if Fess Parker buys French oak direct", which would have
been a wrong premise sent to a stranger.

A single source that returns nothing tells you nothing. A second source
that returns something different tells you the brief was wrong.


### Coverage is not uniform, so the order matters

On Untamed Wine Estates, a 2026-09-24 test:

| Source | People returned |
|---|---|
| Seamless | 5, including the Chairman and a VP |
| ZoomInfo | 3 |
| Apollo | 5, but no LinkedIn URLs on most |
| Lusha | 0 |

**Seamless was deepest on this small private company** and is the one to
reach for first on small US and Canadian businesses. ZoomInfo's strength
is larger companies, intent signals and org structure, which is a
different job.

All four agreed that Tammy Lewis is not at Untamed Wine Estates. When
four sources agree, the brief is wrong, not the databases: either she
self described the company on the webinar registration, or she works
somewhere else. Ask Marcel rather than guessing a URL.

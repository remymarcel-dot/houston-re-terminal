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

## The four source sweep is a checklist step, not a principle

Written 2026-09-24 because the principle was written earlier the same day
and then not followed. Marcel had to ask twice. A principle that needs
remembering is not working; this is the mechanical version.

**Before telling Marcel a person cannot be found, all four must have been
tried and the result stated per source:**

1. **Apollo** `apollo_people_bulk_match` with name plus organization_name.
2. **Seamless** `search_contacts` with **`companyName`**, not `fullName`.
   Name search returns hundreds and buries the answer; company search
   returns the roster with `liUrl` on every row.
3. **Lusha** `prospecting_contact_search`. Fuzzy on surnames, which is
   how Isaac Aframian was found when three others missed the misspelling.
4. **ZoomInfo** `search_contacts`. Takes `firstName`/`lastName` or
   `companyName` as plain strings, and `userIntent` is required.

**Then and only then say not found, and say which four were tried.**

### Two failure modes this catches

**A misspelling in the source list.** Afranian for Aframian hid a $44.3M
importer's VP of Finance from three databases. If several sources return
nothing on a name someone typed by hand, suspect the spelling and search
the surname alone before concluding anything.

**A wrong company in the source list.** Shelly Dunlavey was listed as
Fess Parker Winery. Seamless has her as an accounting assistant at a
Santa Barbara CPA firm. One source returning nothing tells you nothing;
a second source returning something different tells you the brief was
wrong.

### Worked example, the InnoVint attendee list

Three names survived all four sources with no match: Patty Ketchum,
Keith Crawford, Kristina Williams. That is a real answer. The same three
after only Apollo and Seamless would have been a guess.

The sweep also produced a name that was never on the list: searching
Frog's Leap by company rather than hunting Patty Ketchum surfaced
**Shannon McLaren, their CFO**. Searching the company often beats
searching the person.

## Paused is not dead, and campaign stats are not the thread

**2026-09-25.** Campaign 618477 was recorded here as "dead, never to
resume" after it wedged in STARTING on 2026-09-23 and was paused. It
resumed on its own and ran four leads to MessageSent alongside 618489,
the rebuild covering the same ten people.

Two rules:

1. **A paused campaign can resume.** Never write "dead" in the record on
   the strength of having paused something. Re-read the campaign state
   before relying on it. `get_all_campaigns` with statuses IN_PROGRESS,
   SCHEDULED, STARTING, PAUSED and DRAFT gives the whole picture in one
   call and should be run at every inbox sweep, not only when something
   looks wrong.

2. **Campaign level `MessageSent` is not proof a message was sent.** Two
   campaigns holding the same lead can both report MessageSent for a
   single underlying action. On 2026-09-25 the stats implied three people
   had been double contacted; opening the three conversations showed one
   message each. **Before reporting a duplicate to Marcel, open the
   thread and count the messages.** The thread is the record; the
   campaign is a controller.

Both halves matter. The first nearly let a real duplicate through. The
second nearly reported a duplicate that never happened.

## Scheduled is not started, and a launch confirmation does not survive the weekend

On 2026-09-25 campaign **622397**, Play 0 batch 4, was started and confirmed:
`status: SCHEDULED`, 6 pending, 0 failed, with `startDate` 2026-09-28. Marcel was
told it would send Monday at 9am Central.

On Monday morning it read **`status: DRAFT`, `startedAt: null`.** It had reverted
on its own and **sent nothing on its send date.** Restarting it put it straight
to IN_PROGRESS with 6 in progress.

This is the mirror of the "paused is not dead" rule. A campaign confirmed
SCHEDULED days earlier may not be scheduled any more, and a campaign that
quietly reverts to DRAFT produces no error, no failure count and no signal of
any kind. It simply does not send.

**So on every cycle, re-verify the status of every campaign whose send date has
arrived or passed.** `get_all_campaigns` filtered to IN_PROGRESS, SCHEDULED,
STARTING, PAUSED and DRAFT shows it in one call. A campaign missing from the
IN_PROGRESS and SCHEDULED buckets when its date has arrived is the thing to look
for. What caught this one was noticing that batch 4 was absent from the active
list, not any alert.

### A related trap: progressStats.totalUsers is not the lead count while DRAFT

The same campaign reported `totalUsers: 15` while in DRAFT, against a list of 6
leads. Batch 5 reported 12 against 6, Two Brothers 2 against 1. That looked
exactly like duplicated leads, which would be the most damaging failure
available here, and it cost real time to rule out.

Reading the **list** is what settles it: list 969943 held exactly 6 leads, the
right 6, no duplicates. Once the campaign started, `totalUsers` corrected itself
to 6.

**Trust the lead list, not the campaign's counter, and never raise a duplicate
alarm from campaign stats alone.** This is the third version of the same lesson,
after "campaign stats are not the thread" and "failedLeadsCount zero does not
mean everything landed."

## A stale vanity slug imports as a dead lead, and it looks like nothing is wrong

A LinkedIn profile URL that still resolves in a browser can be the **old**
vanity slug, kept alive by a redirect after the person changed their display
name. HeyReach does not follow that redirect. The lead imports with
`addedLeadsCount: 1` and `failedLeadsCount: 0`, and then sits in the list with:

- a `linkedin_id` beginning `imp_` instead of a numeric id
- `headline`, `imageUrl`, `companyName` and `position` all null
- no photo and no enrichment of any kind

Proved on 2026-09-28 with the same person, in the same list, minutes apart:

| URL | linkedin_id | headline |
|---|---|---|
| `cindy-woodstock-82679ba4` | `imp_ZHCZYSBPAIUUJNZELCQFWEFGS` | null |
| `cindy-cross-woodstock-82679ba4` | `372210654` | CFO/HR at IGI Services Inc. |

Same numeric suffix, same person, one enriches and one does not. She had
changed her displayed name, so the slug moved and the old one became a redirect.

**What to do.** An `imp_` id is not a lead. Treat it as a failed import, not a
quiet success, and never let a campaign send to one believing the person was
contacted. Ask for the URL copied **from the browser address bar with the
profile open**, which is the canonical slug, rather than from a search result,
a share link or a saved bookmark, all of which can carry the old one.

**A stale slug is not the only cause.** Candy-Dulce Sifuentes,
`candy-dulce-sifuentes-271a271a7`, fails the same way across three imports, and
Marcel confirmed that URL from the live profile three separate times, so the slug
is current and the name-change explanation is ruled out for her. Passing the slug
as `username` instead of `profileUrl` is not a workaround either: the import is
dropped outright, because a payload without `profileUrl` is rejected silently.

So some profiles simply will not enrich, most likely because of their own privacy
settings or their visibility from the sending account. The lead still sits in the
campaign and will still be attempted. Watch `totalUsersFailed` on the send date,
and if it fails, the fallback is for Marcel to message the person directly from
LinkedIn, which costs him one click and bypasses HeyReach entirely.

## The list index lags the import, so a fresh lead reads as missing

After `add_leads_to_list_v2` reports `addedLeadsCount: 1`, the lead can be
invisible for a short while: `get_leads_from_list` returns nothing for a keyword
match on the surname, nothing for a `leadProfileUrl` filter, and `totalCount`
still shows the pre-import number.

Observed 2026-09-28 with Chris Sadler. The record was in fact created, proved by
re-sending the same lead and getting `addedLeadsCount: 0, updatedLeadsCount: 1`,
and a moment later a keyword search on the **first** name returned him normally.

So: a lead that does not appear immediately has not necessarily failed. Before
concluding an import failed, re-send it once and read the counts. An `updated`
count means it is already there and must not be added again. Do not conclude from
a single empty read that the lead is missing, and do not re-import blindly, which
is how a lead ends up in a campaign twice.

## Two inbox-sweep errors, both made on 2026-09-29

### 1. `seen: false` is the wrong test for "needs attention"

A thread can be marked **read** and still hold an unanswered reply, because the
read flag tracks whether the conversation was opened, not whether anyone answered
it. Filtering `get_conversations_v2` on `seen: false` therefore hides real
prospect replies.

**Jorge Cavazos, President of EXL Automated Solutions, replied at 01:56 on
2026-09-29 and did not appear in a `seen: false` sweep run hours later.** Marcel
caught it: *"there is one reply check it better it is slipping"*.

**The correct test is `lastMessageSender == "CORRESPONDENT"`.** Sweep unfiltered
and apply that in code. Never report an inbox as clear on the strength of the
seen flag.

### 2. Never pull conversations raw at a large limit

`get_conversations_v2` at `limit: 40` returned 130,301 characters and blew the
token budget, because each thread carries the correspondent's full `about` text
and every message body.

**Always post-process rather than reading it inline.** Either keep `limit` at 10
to 15, or take the saved file and reduce it first:

```
python3 - <<'EOF'
import json
d=json.load(open(FILE))          # strip any prefix before the first '{'
for c in d['items']:
    if c.get('lastMessageSender')!='CORRESPONDENT': continue
    p=c.get('correspondentProfile') or {}
    print(c['lastMessageAt'],'|',p.get('firstName'),p.get('lastName'),
          '|',p.get('companyName'),'|',p.get('position'))
    print((c.get('lastMessageText') or '')[:400])
EOF
```

That prints who is waiting, from when, and what they said, in a few lines each.

### And one thing that did work

`autoTags` applied **"Not interested"** to Cavazos automatically at 02:40, tied to
campaign 618515. That is the first time the tagging has been seen working on a
live reply, against the earlier finding that only three tags existed across 294
conversations. Worth checking autoTags on each sweep; it is not reliable enough to
depend on, but it is free signal when present.

## A running campaign picks up list changes, in both directions

Confirmed three times on 2026-09-28 and 09-29, and it is worth relying on:

| Change | Campaign state | Result |
|---|---|---|
| Removed Sifuentes from list 974427 | SCHEDULED | 625479 went 9 to 8 |
| Added Cordon to list 975075 | SCHEDULED | 625896 went 6 to 7 |
| Added Rodriguez Arrizabalaga to list 978548 | **IN_PROGRESS** | 628244 went 2 to 3 |

So a lead can be added to or pulled from a campaign that is already running by
editing its list, without rebuilding anything. Always read the campaign back
afterwards: the change in `totalUsers` is the proof, not the add or delete
response.

**One limit.** `customUserFields` are set at import, so the personalized note
cannot be edited in place. Changing a note means deleting the lead and re-adding
it, which on a live campaign risks disturbing a lead already in flight. Get the
note right before the import.

### A customUserField does update in place on a list whose campaign is still DRAFT

The earlier note here said `customUserFields` cannot be edited in place. That is
too broad. On 2026-09-29, list 978635 with campaign 628299 in DRAFT, re sending
a lead with the same `profileUrl` and a changed `note` returned
`updatedLeadsCount: 1` and the read back showed the new text. The correct rule:

- **DRAFT campaign, or lead not yet reached** — re sending the lead overwrites
  the note. Use it to fix a typo rather than deleting and re adding.
- **Lead already in flight** — the note is compiled into the queued action and
  the overwrite does not reach it. Do not rely on it; stop the lead instead.

Read the lead back either way. The counts alone do not prove the field changed.

### Non ASCII characters survive the import, so do not strip accents

Spanish notes imported with `qué`, `decisión`, `aquí`, `dólares`, `línea`,
`cómo` and `Ángel` all read back intact from `get_leads_from_list`. Writing
Spanish without accents is a self inflicted error that a prospect reads as
carelessness. Send the accented text and verify it on the read back.

### The `imp_` placeholder clusters on long numeric slug suffixes

Three confirmed failures now share a shape: `candy-dulce-sifuentes-271a271a7`,
`jessica-paz-964a92372`, `sergio-marentes-gurrola-12b744260`. All carry a long
trailing suffix rather than the short six to eight character hash of an older
account, and none enriched on two imports, with and without the trailing slash.
Do not keep retrying. Log it, leave the lead in when the send is days out, and
put the name on the verification check so the failure is caught rather than
assumed.

### The `imp_` placeholder is sticky at the workspace level, so the first import is the only one that counts

Proved on 2026-09-29 with `jessica-paz-964a92372`. The sequence of evidence:

1. First import into list 978635 resolved to `imp_ZYDILSBWEVAUDEOVQPBMELKIH`.
2. Re import into the same list with the trailing slash: same placeholder.
3. `get_lead` on the URL returns that same placeholder with every field null
   except `firstName`, `lastName` and `username`. The record is workspace wide,
   not list scoped.
4. Import into a brand new list 978657, this time supplying `username` as well
   as `profileUrl`: `addedLeadsCount: 1`, and the read back shows the **same**
   `imp_` id again.

So a fresh list does not reset anything. Once a URL enters the workspace as a
placeholder, every later import of that URL inherits the poisoned record. Do
not spend more calls on it, and do not present a re import as a fix.

**What this does not yet establish:** whether a placeholder lead actually fails
the send. The campaign action works from `profileUrl`, so it may still fire.
Campaign 626018 carries three placeholders (Olivier, Grappe, Rubio) and sends
2026-10-01; 628299 carries two (Paz, Marentes Gurrola) and sends 2026-10-02.
Thursday's result is the experiment. Read `totalUsersFailed` on 626018 before
Friday and let it decide whether the two in 628299 get pulled for a manual send.

List 978657 is a disposable probe. Do not add leads to it or build from it.

### `AlreadyAConnection` is a different failure from `ConnectionRequestAlreadySent`, and it is a play assignment error

Campaign 625479 failed one lead on 2026-09-29 with `errorCode: AlreadyAConnection`,
`leadCampaignStatusMessage: "Already a connection"`. Ricardo Yllescas, CFO of
Elementia USA, was already first degree, so a CONNECTION_REQUEST could never
land and the personalized note never reached him.

- `ConnectionRequestAlreadySent` means an invitation is pending. Resending fails
  identically. Wait or withdraw. (Patrick Gaughan, El Paso W4.)
- `AlreadyAConnection` means the wrong play was chosen. The person belongs in
  Play 0 as a direct message. Re running Play 4 will never work.

**The check that prevents it.** When Marcel supplies a bare profile URL with no
degree stated, the degree is unknown, and Play 4 is a guess. Either ask him, or
test the URL against `get_my_network_for_sender` before assigning the play. The
09-28 note on this lead already said "if he is already a first degree connection
he belongs in Play 0 as a message, not an invitation" and the lead was still
routed to Play 4. Writing the caveat down is not the same as acting on it.

Recovery is a Play 0 message, held for Marcel to read before sending. A failed
invitation is silent to the prospect, so nothing was burned.

### Past postings in an About section do not trigger the Venezuela stop

The same lead's About text reads "Business Controller for Colombia, Venezuela and
Ecuador, based in Bogota City" as career history, with the current seat being
CFO, Elementia USA, Houston. The Venezuela rule is about where the money moves
now: a current seat that names Venezuela, a company operating there, a
counterparty there. A role someone held years ago is biography, not exposure.
Do not cut on it, and do not mention it to the prospect either.

### A recovery campaign needs the exclusion filter turned OFF

Every cold campaign in this workspace is built with
`excludeContactedFromOtherCampaigns: true`, which is right for new outreach and
wrong for a recovery. When a lead has already sat in a campaign that failed,
that earlier campaign counts as prior contact, so the default filter excludes
the lead from the new one. The campaign then reads `IN_PROGRESS` with the lead
sitting in `totalUsersExcluded`, which looks like success and sends nothing.

Campaign 630456 on 2026-09-30, recovering Ricardo Yllescas from the
`AlreadyAConnection` failure in 625479, was built with the flag set to false
along with `excludeContactedFromSenderInOtherCampaign` and
`excludeHasOtherAccConversations`. Read back: `excludeInOtherCampaigns` false,
`totalUsersExcluded` 0, one user in progress.

**Always read `totalUsersExcluded` after starting, not just the status.** A
status of IN_PROGRESS says the campaign is running, not that anyone is in it.

### `send_message` cannot open a new thread

It requires a `conversationId`, and a lead who has never been messaged has no
conversation. `get_conversations_v2` filtered to the profile URL returns
`totalCount: 0`. So a first message to a first degree connection always goes
through a Play 0 campaign, never through `send_message`. Reserve `send_message`
for replies inside a thread that already exists.

### Never leave a draft file saying "nothing has been sent" after approval

Marcel caught this on 2026-09-30. `drafts-2026-10-05-wave.md` opened with
"held for Marcel's read. Nothing has been sent" and both campaigns marked
DRAFT. He had approved them and they had been started hours earlier. A
"STARTED" line was appended at the bottom of the file, which is not good
enough: the header is what anyone reads first, and a week later it is the
only thing they will remember.

**When a campaign's state changes, fix the top of the file, not just the
bottom.**

### The four states, and why `startedAt: null` is not a problem

- **DRAFT** — built but inert.
- **SCHEDULED** — armed. Fires by itself at the start date, no further action
  needed.
- **IN_PROGRESS** — actively working the leads. `startedAt` now has a value.
- **FINISHED** — every lead has reached an end node.

`startedAt: null` on a SCHEDULED campaign is correct and expected, not a
fault. It only fills in when the campaign actually begins.

**Two true statements to keep distinct, because they get conflated:** a wave
can be **approved and armed** while **nothing has physically been sent**. Say
which one is meant. "It is live" is ambiguous and "it went out" is wrong until
`IN_PROGRESS` with a non null `startedAt`.

## The invitation ceiling is 15 a day, and it binds

`get_linked_in_account_by_id` on 237851 reports `connectioRequestLimit: 15`
against a `connectioRequestMax` of 40, and `messageLimit: 30`. Play 4 draws on
the 15; Play 0 draws on the 30. So a day holding a 15 lead cold wave and a 4
lead Play 0 wave is at the invitation ceiling and nowhere near the message one.
Count the two plays separately before calling a day full.

### Removing a lead from a SCHEDULED campaign

`stop_lead_in_campaign` returns a 500 on a campaign that has not started, so it
is not the tool for this. `delete_leads_from_list_by_profile_url` on the
campaign's list works, **with the trailing slash**, and the campaign's
`totalUsers` follows the list. Two traps seen on 2026-10-01:

- The reads immediately after the delete are stale. The list still showed the
  lead and the campaign still showed 15. A targeted read by `leadProfileUrl` a
  moment later showed him gone. Do not undo a delete because the next read
  disagrees with it; re-read the one lead.
- Sending the URL **without** the trailing slash returns
  `notFoundInList: ["<slug>"]` whether or not the lead is there, so that
  response proves nothing either way.


## A Play 0 MESSAGE needs a real connection, and says nothing when it does not have one

**Proven on campaign 632612, 2026-10-01 to 02.** Two leads, one MESSAGE node,
opposite outcomes:

- **Sean Fightmaster** had failed an earlier invitation as `AlreadyAConnection`,
  so he is a genuine connection. `leadMessageStatus: MessageSent`.
- **Hillary Stroble** had failed as `ConversationExists`, which means a thread
  exists outside HeyReach but she is **not** a connection.
  `leadMessageStatus: None`, `failedTime: null`, `errorCode: null`,
  `leadCampaignStatus: Finished`.

So the node is not flaky. **It requires an actual connection, and when it does
not have one it ends the sequence quietly and records success.** The campaign
counters show zero failures either way.

Two rules follow:

1. **`ConversationExists` is not a route back in.** Neither a
   `CONNECTION_REQUEST` nor a `MESSAGE` will reach that person. Treat them as
   email only from that moment, or send by hand.
2. **Never read delivery off `progressStats`.** Check `leadMessageStatus` or
   `leadConnectionStatus` at lead level. The counters cannot distinguish a send
   from a silent skip, which is precisely how Hillary went uncontacted while the
   campaign reported a clean run.

A corollary worth stating, because the opposite was briefly believed: **Play 0
messages to genuine first degree connections work normally.** There is no reason
to hand-send those for reliability. Hand-sending remains right when the message
is personal enough to warrant it, not because the node cannot be trusted.


## Set the campaign schedule at creation, not after

HeyReach's default campaign schedule is **Mon to Fri, 09:00 to 17:00 UTC**, which
is **04:00 to noon Central**. For a Houston sender that window is both wrong and
short, and it silently delays sends.

**It cost a campaign on 2026-10-02.** Campaign 634581 (Olvin Caballero) was
created without a schedule at 14:37 UTC on a Friday. Its 4 hour delay landed at
18:37 UTC, past the 17:00 cutoff, so the invitation slipped to **Monday**.
`update_campaign_schedule` then refused with `Invalid campaign status`, because a
schedule can only be changed while a campaign is DRAFT, SCHEDULED or PAUSED, and
it was already IN_PROGRESS.

So pass the schedule in the `create_campaign` call, always:

```
"schedule": {"dailyStartTime":"08:00:00","dailyEndTime":"18:00:00",
             "timeZoneId":"America/Chicago",
             "enabledMonday":true, ... "enabledSaturday":false,"enabledSunday":false}
```

Campaign 634669 (Martin Hauser) was built this way an hour later and its
invitation lands the same afternoon.

Two further points. A 3 hour delay on the `CONNECTION_REQUEST` is the API
minimum and buys more room inside the day than 4. And activity timed to Central
business hours looks like a person, which a 4am send does not.


## When a HeyReach write fails, try the v1 lead endpoint before giving up

On **2026-10-02** every HeyReach *write* endpoint started returning a bare
`An error occurred invoking '<tool>'` while every *read* endpoint kept working
normally. Failing: `create_empty_list`, `create_campaign` (three attempts),
`add_leads_to_campaign_v2`. Working: `get_campaign`,
`get_all_linked_in_accounts`, `get_leads_from_campaign`, `get_all_campaigns`.

**`add_leads_to_campaign` (v1) worked on the first try.** So the outage was not
account-wide, not an auth problem and not a quota. It was specific endpoints.

The workaround, in order:

1. **Do not keep retrying the same endpoint.** Two attempts is enough to tell a
   transient blip from a broken endpoint.
2. **Add the leads to an existing campaign that already runs the play you want.**
   A campaign's sequence and schedule are fixed at creation, so any campaign
   running the same play with the same schedule is a valid home for new leads.
   On 2026-10-02 the seven wave 2 leads went into campaign **634736**, built
   earlier the same day with the identical Play 4 sequence, rather than into a
   new campaign that could not be created.
3. **Use the v1 shape**, which differs from v2:

```
add_leads_to_campaign(campaignId, accountLeadPairs=[
  {"linkedInAccountId": 237851,
   "lead": {"firstName":..., "lastName":..., "profileUrl":...,
            "companyName":..., "position":...,
            "customUserFields":[{"name":"note","value":"..."}]}}
])
```
It returns a plain integer: the number of leads accepted. v2 takes a flat
`leads` array instead of `accountLeadPairs` and infers the sender.

4. **Then verify with `get_leads_from_campaign`.** The count alone is not proof.

**Mixing waves into one campaign costs nothing** except that the campaign name
no longer describes its contents, so write the wave number into each pipeline
entry's touch note. The pipeline is the record, not the campaign name.


## An `imp_` lead has not resolved YET, which is not the same as never

`get_leads_from_campaign` returns, per lead, a `linkedInUserProfileId` and a
nested `linkedInUserProfile.linkedin_id`. For a lead HeyReach has resolved
against LinkedIn these are a real URN and a numeric id, with headline, location
and image populated. For one it has not, `linkedInUserProfileId` is `null` and
`linkedin_id` is a placeholder beginning `imp_`, with the rest null.

**An earlier version of this section said such a lead "will not be contacted, and
nothing will report a failure." That was too strong and it was wrong within the
same day.**

On **2026-10-02**, lead 320046646 in campaign 634736, Jose Antonio Martinez Haro
of Divine Flavor, was added carrying `imp_TSULFPKEXCBZMALRKEMLYLFPN` and nothing
else. Checked again six hours later he carried a real
`linkedInUserProfileId`, `linkedin_id` 6534481, his real headline and his
location. **HeyReach resolved him on its own when the `VIEW_PROFILE` step ran.**

So:

- **An `imp_` id at the moment of adding means nothing.** Resolution happens when
  the first sequence action runs, not when the lead is created.
- **Judge it after the first action.** If `lastActionTime` is set and the id is
  still `imp_`, that is a real problem. If `lastActionTime` is null, the lead has
  simply not been reached yet.
- **It is still worth noting at add time**, because a genuinely bad slug produces
  the same symptom at first and fails later with
  `CannotViewProfileDoesnotExist`. That is what happened to Louise Lalor in
  campaign 620518, whose slug `louise-lalor-982467b6` did not exist and who had
  to be re-added as `louise-l-982467b6`.

**The distinguishing test is `lastActionTime`, not the id on its own.**

Being wrong in the pessimistic direction is the cheap way to be wrong here: the
cost was a needless warning on the strongest name in the batch, rather than a
missed send.

## Read every campaign's failure count, because a failure is silent

A sweep of all 46 campaigns on **2026-10-02** found **seven failed leads**. Four
had been caught at the time. **Three had not**, and two of those three were
recorded in the pipeline as if they had been contacted.

The failures are not hidden. `get_all_campaigns` reports
`progressStats.totalUsersFailed` per campaign, and six campaigns were carrying a
non-zero count. Nobody read the field.

**So after any campaign finishes, read its `totalUsersFailed`, and if it is
non-zero pull the leads and read each `errorCode`.** The count alone does not
say who or why.

### The error codes seen so far, and what each one means

| errorCode | meaning | what to do |
|---|---|---|
| `ConnectionRequestAlreadySent` | An invitation is **outstanding right now**, sent earlier from outside this campaign | Send nothing. Nothing was delivered. The date is unknown |
| `AlreadyAConnection` | They are a 1st degree connection, so an invitation is meaningless | Move to a Play 0 message |
| `ConversationExists` | A conversation thread exists but they are **not** a connection | A Play 0 MESSAGE will silently do nothing. Use email or send by hand |
| `CannotViewProfileDoesnotExist` | The profile URL is wrong. The lead also carries an `imp_` placeholder id | Re-copy the slug and re-add |

`ConnectionRequestAlreadySent` is the dangerous one, because it looks like a
near miss and is actually two separate facts: the person **has** a pending
invitation, and your note **was not delivered**. Recording such a lead as
`invitation-sent` is wrong twice over. Use
`status: invitation-pending-origin-unknown` and set the touch date to the string
`"unknown"`.

### Validate a URL you did not get from Marcel before you use it

The rule is never to construct a LinkedIn URL. A URL found by **web search** is
not constructed, but a search listing is not proof either, which is what left
the Avi Nir URL unusable on 30 September.

**`get_lead` settles it, and it is read-only.** Pass the candidate URL; if it
returns a real `linkedin_id` with the name, company and position matching what
was expected, LinkedIn itself has confirmed the slug belongs to that person.
This confirmed Fraymil Rodriguez (`50440430`, COO Exp. Group LLC) and John P.
Olivo (`15465923`, President and CEO Fresh Express, with his full Chiquita
history). A wrong URL simply returns nothing and no message is sent either way.

`get_campaigns_for_lead` takes the same URL and answers "which campaigns is this
person in" in one small call, which beats pulling 46 lead lists. Note its
parameter is `profileUrl`, not `leadLinkedInId`.


## Verify the same afternoon and you will verify nothing

Checked all five of 2026-10-02's campaigns at roughly 17:30 UTC, about two hours
after the last was built. **All 18 leads read `leadConnectionStatus: None`.**
Nothing had been sent, and nothing was wrong.

The sequence is `VIEW_PROFILE` then `CONNECTION_REQUEST` **at a 3 hour delay**,
which is the API minimum. So a campaign started at 15:30 UTC cannot send an
invitation before 18:30 UTC, and HeyReach works leads **serially**, spacing the
profile views out: on 2026-10-02 the fourteen leads of campaign 634736 were
viewed between 15:44 and 17:20, so their invitations were due across a span of
18:44 to 20:20.

**So the useful verification window is the next morning, not the same afternoon.**
Checking too early produces a wall of `None` that means only "the delay has not
elapsed," and reading it as failure is how a working campaign gets rebuilt into a
duplicate.

Two things worth reading early, though, because both are real signals:

- **`lastActionTime: null`** means the lead has not been reached at all yet, which
  distinguishes "waiting on the delay" from "waiting in the queue."
- **`errorCode`**, which appears as soon as a step actually fails and does not
  wait for the sequence to finish.


## A get_lead 404 is not proof the URL is wrong

Confirming a search-derived profile URL with `get_lead` worked on six people on
**2026-10-02** and failed on one: **Rosa Duarte of California Giant Berry Farms**,
404 twice, with and without the trailing slash.

The URL is almost certainly right anyway. **LinkedIn's own page at that address
carries her name, title and company in the page title**, and the page's schema
markup gives the same slug as `sameAs`. The likely cause is that she is a small,
low-activity profile — 333 connections, 347 followers — that HeyReach cannot
resolve.

So the three outcomes are distinct and should be recorded differently:

| get_lead result | meaning | what to do |
|---|---|---|
| Real `linkedin_id` with matching name, company and position | LinkedIn has confirmed the slug | Use it anywhere, campaign included |
| **404** | **Unresolvable, not necessarily wrong** | Send BY HAND only. Do not put it in a campaign until a human has looked at the profile |
| Returns a **different** person | the slug is wrong | Discard it |

**The reason the distinction matters is the failure mode at the other end.** An
unresolvable URL in a campaign becomes an `imp_` placeholder lead that is never
contacted and never reports an error, which is exactly what happened to Louise
Lalor in campaign 620518 on a slug that did not exist. Sending by hand carries no
such risk, because a wrong URL simply fails to open.


## To change a queued lead's note, use v2. NEVER stop the lead first

**`add_leads_to_campaign_v2` updates an existing lead's custom fields in place.**
Call it with the same `profileUrl` and the new `{note}` value and it returns
`{"addedLeadsCount":0,"updatedLeadsCount":1,"failedLeadsCount":0}`. The queued
invitation keeps its place and simply carries the new text.

**`stop_lead_in_campaign` has no API inverse.** There is no resume-lead tool. Once
a lead is stopped or paused, only the HeyReach web UI can restart it.

**This cost a send on 2026-10-02.** Asked to add a line to Gloria Mancilla's
queued note, I called `stop_lead_in_campaign` first on the assumption that the
lead would have to be replaced. Then:

- **v1 `add_leads_to_campaign` returned `0`** — it will not re-add a profile that
  already exists in the campaign, even when that existing row is paused.
- **Every other Play 4 campaign refused her**, because 630877, 630953 and 628299
  all carry `excludeInOtherCampaigns: true`, and her paused row in 634736 counts
  as being in another campaign.
- **v2 then updated the note in place anyway**, which is what should have been
  done first and would have required no stop at all.

So she ended with the right note and a paused row that needs a human click.

**And a UI resume may not stick, so stop fighting it and send by hand.** Marcel
resumed her in the HeyReach UI on 2026-10-02 and `get_campaigns_for_lead` still
returned `"leadStatus":"Paused"` on three checks afterwards, queried both by
`profileUrl` and by `linkedinId`. Whether that is API lag or a failed resume is
unknowable from here, and it does not matter: a lead whose status will not come
back is a one-click manual invitation. Hand Marcel the URL and the note text,
tell him to leave the paused row alone (a resumed row would try to send a second
invitation; even if it fired, LinkedIn rejects the duplicate and HeyReach logs
`ConnectionRequestAlreadySent`, a harmless Failed row), and log the touch when he
confirms. Do not spend further turns verifying a status you cannot change.

**The order of operations:**

1. **Changing a note on a queued lead → v2 update, nothing else.**
2. **Genuinely removing someone → stop the lead, and accept it is one-way.**
3. Check `leadStatus` after any such change. `Paused` means it will not send,
   however correct the copy now is.

### A second thing worth knowing

`stop_lead_in_campaign` takes `leadMemberId` (the numeric `linkedin_id`, e.g.
`336966191`) **or** `leadUrl`. Passing a profile URL as `leadMemberId` returns a
404, which looks like "lead not found" and is really "wrong field".

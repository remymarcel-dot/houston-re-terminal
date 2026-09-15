# The four plays

Run them in this priority order. A cycle usually touches two or three,
not all four.

---

## Play 1 — Inbox revival

**Why first:** these people already responded to something. They are
further along than anything a new campaign produces this month.

There are ~221 existing conversations. Two groups matter:

- **Waiting on Marcel** — the correspondent sent last and it is a real
  prospect. Draft his reply. Nothing outranks this.
- **Stalled** — Marcel sent last, no reply, >7 days old. One follow-up,
  using the concrete rate-comparison offer from `voice.md`, not a
  "checking in".

Known live threads as of Sep 15 2026 (verify current state before
acting, these move):

| Person | Role | State |
|---|---|---|
| Elena Tavares | CFO, Monte Vista Farming | Connected, corridor question sent, awaiting reply |
| Luz A Rodriguez | Controller, Square One Farms | Replied "Thanks Marcel", thread stopped |
| Nelson Peixoto | VP Finance Americas, EagleBurgmann | PT message sent Sep 15 |
| Clemens Taschée | Director Finance, RINGANA | Connection note sent, EUR/USD hub angle |
| Jennifer Ayers | VP Customs Ops, T H Gonzalez | Met at El Paso summit, connected |

**Cap:** no volume limit worth worrying about — there are only so many.
Quality of the reply is the whole game. This play is Tier 3: every reply
to a live human gets drafted and shown to Marcel before it sends.

---

## Play 2 — Network mining

**Why it matters most long-term:** ~21,778 first-degree connections can
be messaged directly. No connection request, no acceptance gate. Against
a 40 messages/day cap this is a multi-year runway, and it converts far
better than cold.

Procedure: segment per `references/icp.md`, research each, draft a
message that opens on something true about them, present for approval,
send the approved set.

Because these are existing connections, the opener is different from
cold — acknowledge the existing link honestly. Something in the shape
of: they connected a while back, he has since moved to Monex USA and
works on X, and here is the one question. Don't pretend to a
relationship that isn't there, and don't pretend there's none when
there is.

**Cap:** whatever `references/config.md` sets for the current ramp week.
Build the campaign, pre-write a personalized opener per lead as a custom
field, get the one approval, let HeyReach pace the sending.

---

## Play 3 — Event-driven outreach

**Why it works:** a named event is a real reason to reach out, and it
sidesteps the cold-open problem entirely.

Live angles:

- **North America Manufacturing Expo & Summit** — San Antonio, Henry B.
  González Convention Center, April 15-16 2026. Marcel is attending.
  Target: exhibitors and attendees in manufacturing, automotive,
  aerospace, electronics, medical devices, cross-border trade. Before
  the event: "I'll be there, worth meeting?" After: "we met / we both
  attended".
- **Mexico's Supply Chain Nearshoring Summit, El Paso** — already
  happened. Follow up with anyone from the B2B meetings who hasn't been
  contacted since. Dr. John Min's Economic and Trade Outlook 2026 talk
  is a legitimate thing to send.
- **Monex USA 2026 Annual Currency Outlook** — an actual document,
  genuinely useful, and the cleanest no-pressure opener available.

---

## Play 4 — Cold prospecting

**Run this last, and fix it before running it.**

The Q3 2026 campaign (`552667`) sent 18 connection requests and got 1
acceptance. **5.6%.** The sequence copy downstream is good — it's the
connection note that failed.

The diagnosis is visible in the data. The campaign's note was templated
around `{FIRST_NAME}` and `{COMPANY}` and led with Marcel's own role:

> Hi {FIRST_NAME}, I lead FX and cross border payments at Monex USA here
> in Houston. Given {COMPANY}'s international footprint, thought it was
> worth connecting.

The hand-written notes in the inbox — Elena, Luz, Clemens — got accepted
and replied to. They lead with something observed about *the recipient*
and mention Monex second.

**So:** pre-generate a personalized note per lead into a custom field
before launching, rather than relying on a `{COMPANY}` merge template.
Same automation, real personalization. Fewer leads, better ones — drop
anyone with no findable hook. The downstream two-message sequence from
`552667` is good and can be reused via `create_campaign_from_template`.

**Cap:** 25 connection requests/day (rising toward 40 as the account
warms). Withdraw unaccepted requests after 21 days, as the existing
campaign already does.

---

## Sequencing a week

A reasonable rhythm, if asked to run this on a schedule:

- **Monday** — full inbox triage, reply drafts, week's target list
- **Tue/Wed/Thu** — network mining, 15-20 drafts a day
- **Friday** — follow-ups on stalled threads, log outcomes, weekly numbers
- **Cold campaigns** — launch at most one at a time, let it run, don't stack

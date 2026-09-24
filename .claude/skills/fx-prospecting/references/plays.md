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

## Play 0: message the connections who were never spoken to

This sits above everything else. The LinkedIn archive (`data/fx/linkedin/`)
showed 1,368 people accepted a connection request in 2026 and never received
a single message, while the reply rate when Marcel does write is 20.9%.

These are first degree, so they cost no invitation quota and carry no
acceptance risk. Work `targets-tier-a.csv` first, then `targets-tier-b.csv`.

Order of work each day:
1. `unanswered-signals.csv` first. Someone gave a phone number or an email
   and got no answer. Nothing else in the pipeline is warmer.
2. `warm-dormant.csv` next, where they replied and it went quiet.
3. `targets-tier-a.csv`, the never messaged finance decision makers.

The opener for a never messaged connection cannot pretend there is history.
There is none. Name the reason they are connected, say the one thing that is
true about their exposure, and ask a question. Four lines.

Do not send a template. The archive is explicit about this: one mass template
went to 668 people and was accepted 5% of the time, while hand written notes
in the same account run 17 to 25%.

## Connection notes

Test blank invitations against hand written ones on the same segment before
assuming a note helps. In 2026 the no-note invitations were accepted 32 to
54% of the time against 5% for the mass template, and 60 to 67% of those
acceptances were CFOs, presidents and owners, so the quality held. The
comparison is across months rather than controlled, so it is a reason to
test, not a settled answer.

## Open loops where Marcel spoke last

The archive screen for buying signals only caught threads where the
prospect sent the final message. That misses a whole class, and the miss
was expensive: Sanoxlabs, Inc, Sergio E Manriquez gave his email within
forty minutes and then volunteered his own flow structure, North America
to Mexico now and Mexico to North America starting in a few weeks. Marcel
answered well and the thread stopped. Because Marcel spoke last, it never
appeared on any list.

A thread is an open loop when the prospect gave something real, an email,
a phone number, a timeline, a structure, and nothing has happened since.
Who typed last is irrelevant. Sweep for both directions.

The most valuable ones carry a date the prospect named themselves. "In a
few weeks" said in August is a live trigger in September, and repeating
their own words back is the strongest possible reopen because it proves
the first conversation was actually heard.

## Never end on a calendar link

Two threads died the same way. Jerome Soitel agreed to four calls across
five months and every one died at scheduling, which only moved when the
calendars came out and Marcel asked for a mobile number instead.
Sanoxlabs, Inc, Sergio E Manriquez went silent immediately after a
Calendly link, having been fully engaged one message earlier.

A calendar link asks a busy person to do the work of choosing. Offer
something concrete instead, propose specific times, or ask for their
number. Reserve calendar links for people who ask for one.

## "Marcel spoke last" is not the same as an open loop

A ranking that treated Marcel's message being last as a strong signal was
wrong, and reading the threads caught it before ten bad drafts went out.
Nine of the first ten ranked that way were conversations Marcel had closed
correctly after the prospect declined:

- Villa Seafood, Inc., Geir Myklebust: partners invoice in USD, equity
  funded, credit insured, has an unused bank line. A textbook clean no,
  closed gracefully.
- colonet fresh organic, Ramiro Gutierrez: already a Monex client.
- VALENCIA INTERNATIONAL, Memo Valencia and Chazey Partners, Edgar
  Paralizabal: explicit declines.
- Combs Wholesale Produce, Ben Combs: buys through US brokers, volume is
  domestic.

Writing again to any of them would undo work Marcel did well.

So classify the prospect's LAST message before ranking anything:

| their last message | meaning |
|---|---|
| a decline, and Marcel closed politely after it | finished, never reopen without a trigger |
| an anniversary or "great to connect" pleasantry | noise, not engagement |
| an inbound pitch at Marcel | not a prospect |
| they left the company | trigger, but for wherever they are now |
| an explicit yes, a phone number, an email, a time | **the only real open loop** |

Only the last row is worth a reopen, and it is rare: nine out of 178.

## Read what the exchange is about, not the shape of the sentence

ClearCloser, Marson Cunha wrote "Absolutely. Could you please send me your
email and/or phone number?", which scored as a strong buying signal. The
thread was about joining an association and an event he had already
attended. Nothing to do with FX.

A phrase that looks like agreement only counts when it answers what Marcel
actually proposed. Before treating any yes as a signal, check what the
preceding message asked. Pattern matching on "yes", a phone number or an
email address finds every warm sounding sentence in the archive regardless
of its subject, and each false one costs Marcel a correction.

## A yes is not a behaviour

WARDENHALL Financial Group, David G. Wong replied "Si lo hacemos" inside an
eleven message thread, which scored as one of the strongest rows in the
archive. Marcel closed it in five words: not responsive.

Two things were being read as strength that are not. A long thread can mean
engagement or it can mean someone agreeable who never moves, and the
archive cannot tell them apart. A literal yes measures politeness at least
as often as intent.

Jerome Soitel is the same shape: four agreed calls across five months, none
of which happened.

So when a name carries agreeable language but no meeting, no number, no
email and no next step that ever landed, treat it as a pattern rather than
a prospect, and ask Marcel before drafting. He has the one input the
archive does not hold, which is how the person actually behaves.

## Count Marcel's unanswered follow-ups before calling anything open

MesoCaribe Energy, Ron Chamness said "I would be open for a call" and that
was scored as an open signal. It was his only reply across eleven messages.
Marcel had already chased five times after it, ending in a clean no-ask
close that told Ron not to reply.

The detector read their last message and ignored everything Marcel sent
afterwards. That is the whole error. Before calling a thread open:

1. Find the prospect's last reply.
2. Count Marcel's messages since. **Two or more unanswered means dead**,
   whatever the reply said.
3. Read his final message. If it is a graceful close, the thread is
   finished and reopening undoes good work.

Marcel's closes are deliberate and well written. Villa Seafood, Inc.,
MesoCaribe Energy and Romero Brands were all ended properly on purpose.

And reachability qualifies on its own. Whether the company has exposure
does not matter if the person will not answer; a real signal is one that
survives contact, not one that sounds willing.

## The ineligible prospect who becomes the channel

Fátima M. could never have been an account. Persona física in Veracruz,
outside Monex USA's reach, ineligible for factoring, and she asked
directly whether the call was just a sales pitch.

On 2026-09-21 she offered, unprompted, to write a post from her own
perspective on working capital in Fresh Produce, recommend Marcel inside
it as a resource rather than as advertising, and channel qualifying US
constituted importers and exporters to him directly.

What produced that, in order:

1. **An opener built on something she actually published**, a 4.84% net
   margin and a 19 day cash cycle, not a product pitch.
2. **Six exchanges of real technical conversation** where she taught
   Marcel more about lime margins than he taught her about FX.
3. **A direct honest answer** when she asked whether this was a sales
   pitch: no, and I could not sell you an account even if I wanted to.
4. **A written summary with real numbers**, including the unflattering
   two to three week onboarding, given freely with nothing asked back.
5. **Commission never mentioned**, on Marcel's explicit instruction,
   across eight exchanges. She has never raised it either.

The lesson worth keeping: **an ineligible contact with an audience in the
right industry can be worth more than an account.** Screening for
eligibility decides what can be sold, not whether the conversation is
worth having. Someone who cannot buy can still be the reason twenty people
do.

When the channel produces a lead, it still passes the same US entity test
as any other. A referral is a warm introduction, not an exemption.

## Ask Marcel who he has already met before sending a cold opener

A database says a person is new. It does not say Marcel has never shaken
their hand.

On 2026-09-22 the El Paso sourcing produced **ROM Industrial, Roman
Bojorquez** out of Seamless, and an opener was drafted for him as a
stranger. Marcel: *"roman yo le conoci en el ultimo el paso expo en marzo
asi que podria ser mas friendly deciendo que sera un gusto
reecontrarlo"*. He had met the man in person in March. The same day,
Marcel supplied the Intercast seat that no database could return.

**The rule.** When sourcing for an event Marcel has attended before, or
in a city he works, put the list in front of him and ask which ones he
already knows before writing a single opener. It costs one message and it
is the difference between a cold request and a reconnection.

**Why the message has to change, not just soften.** A reconnection note
that carries a business question makes the reconnection look like the
pretext for the question, and the recipient feels that immediately. A
warm note does one job: being glad to see them again, and naming where
you will be. The business question waits for the reply, where it reads as
conversation instead of as the reason you wrote.

Cold openers earn the right to ask something in the first message,
because without the question there is no reason to write at all. Warm
ones do not need it and are weakened by it.

## Referral sources get a handshake, not a campaign

Marcel, 2026-09-22, on the economic development and trade bodies at the
El Paso summit: *"for the referral I think is best to just go over the
boot and say hello isntead of doing a campaign, i think is better"*.

He is right, and the reason generalises.

A pre event LinkedIn approach exists to buy a meeting slot from someone
whose time is scarce and who has no reason to give it. A trade
association or economic development agency has the opposite problem: they
are staffing a booth precisely so people will walk up. Sending them a
connection request first is asking permission for something already on
offer, and it starts the relationship in the weakest register available.

**The rule.** Decide the medium from what the person is at the event to
do.

- **Prospects** are there to sell to their own customers. Their time is
  spoken for, so buy the slot in advance: LinkedIn, then matchmaking.
- **Referral sources** are there to meet people. Walk up.

**What makes the booth visit worth anything.** Turning up and being
pleasant produces nothing. These organisations hold one asset worth
having, which is a map of who operates in their region:

- **EL PASO FOREIGN TRADE ZONE**, stand 46, knows every company operating
  inside the zone, which is a list of US entities importing at volume.
- **MVEDA NEW MEXICO BORDERPLEX**, stand 106, knows the manufacturers who
  have landed in Santa Teresa and Dona Ana County, including who arrived
  recently.
- **TEXAS MANUFACTURING ASSISTANCE CENTER**, stand 146, works directly
  with small and mid sized Texas manufacturers, which is the exact ICP.
- **INDEX JUAREZ**, stand 125, is the maquiladora association. Its member
  list is effectively a directory of US companies with Juarez operations,
  read from the Mexican side.

So the ask at the booth is never "can we work together". It is a specific
question about who they serve, followed by an offer they can say yes to
without a meeting: the currency outlook, a conversation with their
members, a joint session. The thing to leave with is a name, not a
business card.

**INDEX Juarez needs one caution.** The association is Mexican and so are
its members as legal entities. The prospect is the **US parent** behind
the maquiladora, never the Mexican operating company. Ask about the
companies, not the members.

## Check the pipeline for prior contact before drafting, not after

Learned 2026-09-23, caught by luck rather than by process.

Katie Dubon at Bravo Foods USA was pulled from the accepted since March
worksheet into Play 0 batch 2 and given an opener reading *"we connected
a while back and I never wrote, which I should have."* She had been
written to twice: once in July or August, and a second touch on
2026-09-16, seven days earlier. A third message opening on the premise
that Marcel had never written would have been visibly false to her.

It surfaced only because `pipeline.json` refused to add a duplicate name
at the logging step, which happens *after* drafting and after the
campaign is built. She was stopped in campaign 618515 with
`stop_lead_in_campaign` before the message node fired.

**The two files say different things and neither is a substitute for the
other:**

- A **target worksheet** like `accepted-since-march-2026.md` says who is
  qualified and believed unmessaged. That belief can be months stale.
- **`pipeline.json` is the record of what was actually sent.** It is the
  only authority on prior contact.

**So: screen every name against `pipeline.json` before writing a single
opener.** One pass over the names at the start of a batch costs nothing.
Discovering it at the logging step means the campaign is already built
and the only remedy left is stopping a lead mid flight.

This is the same failure as Franklin Packaging and as Derek Murphy at
MGS, in a new place. The pattern is always the same: a name reaches a
draft without anyone asking what has already been said to that person.

### Stopping a lead after a campaign has started

`delete_leads_from_list_by_profile_url` fails once a campaign is running,
with "The list you selected cannot be currently modified because it is
used by a running campaign". Use **`stop_lead_in_campaign`** with
`campaignId` and `leadUrl` instead. Confirm it worked by reading
`totalUsersManuallyStopped` on the campaign.

Note the URL format: that endpoint wants the full
`https://www.linkedin.com/in/username/` form. The `http://` and no
trailing slash form that Apollo returns is rejected.

## Campaign STARTING is often just latency, not a wedge

Campaign 618515 sat at `STARTING` with zero users for over two minutes
and then reached `IN_PROGRESS` with all thirteen. Do not rebuild on the
first slow poll. The genuine wedge, 618477, was distinguishable: after
five minutes it still had `startedAt: null` and held only the two leads
added to its list after creation, never the full set.

## Screen by COMPANY against the inbox, not just by person against the pipeline

Learned 2026-09-24, one day after the weaker version of this rule was
written, and the weaker version did not catch it.

Yesterday's rule said: screen names against `pipeline.json` before
drafting. That rule caught Katie Dubon, because she was the same person
already in the pipeline. It could not possibly have caught this:

**F&S Fresh Foods.** Malcolm Pais, Director of Finance, was drafted into
Play 0 batch 2. The company already had a live thread with **Jenna
Bussard, Corporate Controller, in the same Vineland NJ office**: three
messages on 2026-05-27, 2026-09-16 and 2026-09-21, all unanswered, the
last one three days before Malcolm's was due to fire. A fourth approach
to the company, aimed at the colleague sitting next to her, three days
after the third went unanswered, reads as a machine working a list.

Two reasons the name level check was blind to it:

1. **Malcolm is a different person.** A name comparison finds nothing.
2. **Jenna was not in `pipeline.json` at all.** She existed only as a
   HeyReach conversation. The pipeline holds what the plays sent; the
   inbox holds everything, including threads that predate the pipeline.

### The check that actually works

Before any batch goes out, normalize company names and cross reference
**every target company against every conversation in the inbox**, not
just the target people against the pipeline. Fetch all conversations in
pages of 100, which saves to a tool results file rather than context, and
diff company names in a script.

Run it on the whole batch at once. It took one pass over 268
conversations and 24 targets to find exactly one collision, and that one
collision was a message about to go to a company that had already gone
quiet three times.

### Normalizing matters

Strip `LLC`, `Inc`, `Ltd`, `Corp`, `Company`, `Group`, `USA` and
punctuation before comparing. "F&S Fresh Foods" in one record and
"F&S Fresh Foods, LLC" in another must collide, or the check silently
passes.

### What to do with a collision

Stop the new one, not the old one. The existing thread has history and a
standing offer; the new approach has neither. Then decide whether the
company is genuinely worth a second seat, and if it is, wait long enough
that it does not read as pressure, and never open with a line claiming
Marcel has not been in touch, because the company knows otherwise.

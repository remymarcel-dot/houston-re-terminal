# Three data sources, and the order to use them

> **ORDER CHANGED 2026-09-30.** Marcel: *"zoominfo i have no cap as is a
> corporate membership from monex usa."* **ZoomInfo is uncapped and therefore
> goes FIRST.** Everything below that describes Apollo as the first stop was
> written before that was known. Apollo is now second and Seamless third.
>
> This is not a small reordering. ZoomInfo returns, in one call, everything
> the other two return separately: **verified business email, direct dial,
> mobile, job title, LinkedIn URL, and a contact accuracy score** that says
> whether the person is still reachable in that seat. It caches for a year.
> And it costs nothing at the margin.
>
> **The practical consequence: contact data is no longer the constraint on
> the cadence.** The earlier readiness note said touch 2 was impossible for
> 93 of 98 live prospects and framed it as a cost decision. With an uncapped
> source that framing is wrong. The whole pipeline can be enriched for email
> and phone. What limits the cadence now is Marcel's time and the quality of
> each touch, not the data.
>
> **Revised order:**
> 1. **ZoomInfo.** Uncapped. Email, phone, mobile, accuracy score, LinkedIn
>    URL, one year cache. Use it for everything by default.
> 2. **Apollo.** 3,897 lead credits. Better company level search and NAICS
>    filtering for finding people in the first place, and it returns revenue
>    and headcount that ZoomInfo's contact enrichment does not. Use it to
>    *discover*, then ZoomInfo to *enrich*.
> 3. **Seamless.** Marcel, 2026-09-30: *"seamellesai is the free version so
>    not that much of credits but as the last source when we do not find in
>    apollo and zoominfo is good."* It is the **free tier**, 109 credits
>    until 2026-10-26. Last resort only, for names the other two both miss,
>    which on the first run means people like Pablo Ortiz Rodea and Marie
>    Engels who came back as company only matches.
>
> **Apollo's direct dial pool being exhausted until 2026-10-07 no longer
> matters**, because phones come from ZoomInfo now.

Marcel, 2026-09-30: *"you can use apollo, zoominfo and seameless ai. Not only
apollo."*

## Balances checked 2026-09-30, and they overturn an earlier assumption

| source | what is left | resets |
|---|---|---|
| **Apollo lead credits** (enrichment, email) | **3,897 of 4,005** | 2026-10-07 |
| **Apollo direct dial credits** (phone) | **0 of 4,000. EXHAUSTED.** | 2026-10-07 |
| **Seamless universal credits** | **109** | 2026-10-26 |
| **Seamless intent credits** | 2 | none |
| **ZoomInfo bulk credits** | not exposed through the API | unknown |

**Correction.** The agent told Marcel earlier that enriching twenty to twenty
five names "costs roughly 20 to 25 credits", framed as a decision to weigh.
With **3,897 lead credits available** that framing was wrong. Email enrichment
is effectively unconstrained at this pipeline's volume. There was no decision
to weigh; the answer was simply yes.

**The real constraint is phone, not email.** Apollo's direct dial pool is
fully spent this cycle. It resets 2026-10-07.

Whether that matters depends on the cadence: touch 4 is the first call, at
day 10. Friday's wave reaches touch 4 around 10-12 and Monday's around 10-15,
both **after** the reset. So there is no crisis, only a sequencing rule: **do
not promise a phone number before 2026-10-07 unless it comes from ZoomInfo or
Seamless.**

## The waterfall

1. **Apollo first, for email and for LinkedIn URLs.** 3,897 credits, 1 per
   person, and the 2026-09-30 batch showed it also returns the profile URL,
   which removes the manual LinkedIn hunt. Check `has_email` on the free
   people search before spending, so a credit is never burned on a record
   with nothing in it.
2. **ZoomInfo second**, for anyone Apollo misses and for **phone while Apollo
   is dry**. Its decisive advantage: **once a contact is enriched, further
   enrichments of that contact are free for one year.** For names that will
   be touched nine times over months, that makes it the durable place to
   resolve someone. It also returns `contactAccuracyScore`, which is a
   direct read on whether the person is still in the seat, the exact failure
   that produced Steven Wojtowicz and Camilo Ronderos.
3. **Seamless last.** Only **109 credits** and they do not refresh until
   2026-10-26, so it is the scarce one. Reserve it for names the other two
   both miss.

## Two things to know about the Seamless account

- It authenticates as **mremy@camseb.net, Camseb Professional Services**,
  Marcel's own consultancy, not the Monex account. Data pulled there lands in
  that workspace. Not a problem, but worth knowing which account is being
  drawn down.
- Feature access includes Engage, campaigns and AI agent emails. **Those are
  not to be used to send anything.** Per the standing arrangement, the agent
  drafts email and Marcel sends it. Having the capability does not change the
  rule.

## Never spend before the free check

All three expose a free way to see whether a record holds an email or a phone
before any credit moves:

- Apollo: `has_email` and `has_direct_phone` on the people search.
- ZoomInfo: `requiredFieldsList` on `search_contacts` filters to records that
  actually have email, directPhone or mobilePhone.
- Seamless: `search_contacts` before `research`.

Spending a credit on a record with nothing in it is the one avoidable waste,
and all three make it avoidable.

## The accuracy score earned its place on the first run

ZoomInfo returns `contactAccuracyScore`, a 0 to 99 read on whether the person
is reachable and still employed there. On the very first batch, 2026-09-30, it
paid for itself twice:

| who | score | what it meant |
|---|---|---|
| Marcelo Sada | **98**, updated the previous day | Freshest and most reliable record in the batch |
| Roman Rariy | 95 | Solid |
| Rich Wright | 94 | Solid |
| Guillermo Martinez | 93 | Solid |
| **Jimmy Alvarez** | **50** | ZoomInfo is not confident he is reachable. **This independently confirmed the screen's own doubt**: no profile photo, no posts, President since 1980 |
| **Avi Nir** | **50**, and no job title returned | Low confidence, though Marcel had separately confirmed the seat |

That score is the closest thing available to an automated check on the failure
that produced Steven Wojtowicz and Camilo Ronderos. **Read it on every
enrichment.** Below about 70, treat the record as unconfirmed and prefer the
channel that fails quietly, a LinkedIn invitation, over the one that does not,
a phone call.

## Record the do not call flags, always

ZoomInfo returns `directPhoneDoNotCall` and `mobilePhoneDoNotCall`. Two came
back true on the first batch: **Roman Rariy** and **Jimmy Alvarez**, both on
mobile. These are written into `pipeline.json` as `doNotCall`.

**Never hand Marcel a number flagged do not call.** It is his licence and his
reputation on the line, not the agent's.

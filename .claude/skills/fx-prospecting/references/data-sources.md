# Three data sources, and the order to use them

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

# Headline enrichment: run, measured, stopped

Marcel's call, 2026-09-25, after seeing the first batch measured.

## What was tried

`get_leads_from_list` returns a populated `headline` where
`get_my_network_for_sender` returns `headline: null` for all 22,115 records. So
pushing decision seats through a HeyReach list and reading them back enriches
them for free. The plan was 1,802 US decision seats at plausibly operating
companies, in 19 batches of 100, into list **969766**.

## What it cost and returned

One batch ran. 110 records enriched.

| | |
|---|---|
| headline populated, before | 0 of 22,115 |
| headline populated, after | 109 of 110 (99%) |
| `about` populated, before | 17% of the network |
| `about` populated, after | 39% of the batch |
| would have qualified on company name alone | 2 |
| qualified once headline and about were readable | 8 |
| **newly visible** | **6** |

Of those six: one already in the pipeline (3Pete Logistics, Steve Peterson),
one agricultural **software** company (Agriful Software, Patrick Crowley), one
executive search firm (Alder Koten, Silvia Flores), one cross-border **wealth
manager** (Alterna Securities, Alejandro Mateos), one large public company that
already runs a treasury desk (Advance Auto Parts, David McCrary, VP Treasurer),
and one plausible new lead (ACEBRI, Juan Camilo Briceno).

**So roughly one real new lead per hundred enriched.**

## Why it was stopped

The estimate given to Marcel before the run was that enrichment would take 143
qualified leads toward the projected 450 to 700. **That estimate did not
survive the first batch.** At this yield, finishing all 1,802 produces perhaps
twenty to thirty more names, not three hundred.

Set against 138 qualified signing seats already sitting unused, which is about a
month of Play 0 at zero invitation cost, the grind was the wrong use of the
effort. Marcel's decision: stop, work the 138.

## Caveat on the measurement, stated fairly

The slice was sorted by company name, so batch 1 is entirely companies
beginning with "3" and "A". **That is not a random sample**, and a
produce-heavy stretch of the alphabet could read very differently. One per
hundred is a weak estimate, not a settled number.

What should generalize is the *shape* of the false positives, since it does not
depend on the alphabet: agricultural software, consulting, executive search,
wealth management and large public companies all match a cross-border keyword
without being companies that buy foreign currency.

## Two mechanical findings worth keeping

1. **`failedLeadsCount: 0` does not mean everything landed.** The batch reported
   99 added, 0 failed, from 100 sent. Two were missing:
   `leandro-casta%C3%B1o-a9601b8` (percent-encoded ñ in the slug) and
   `zaarath-prokop-6782632`. Neither was reported as a failure. **Only comparing
   the list back against the source file catches this.**
2. **Accented characters in profile URLs are a recurring failure.** Same family
   as the accented-slug problems seen before. Worth handling explicitly if
   enrichment is ever resumed.

## If it is resumed later

Do it after there is reply-rate data from batches 4 and 5, not before. By then
the filter can be aimed at the sectors that actually convert rather than run
blind across every decision seat. List 969766 holds the 110 already enriched and
is named "do not campaign" so it cannot be mistaken for a target list.

# First-degree pool sizing — full pass
Date: 2026-09-25. Source: HeyReach `get_my_network_for_sender`, sender 237851, all 222 pages.

## What the full pass actually measured

| | count | share |
|---|---|---|
| First-degree connections, deduplicated | 22,115 | 100% |
| Have a company name on record | 15,736 | 71% |
| Have a job title on record | 15,443 | 70% |
| Sit in a decision seat (CFO, controller, treasurer, CEO, COO, owner, GM, president) | 5,771 | 26% |
| Decision seat **and** a visibly cross-border business | 224 | 1.0% |
| After removing people and companies already worked | **199** | **0.9%** |

Enumeration note: 22,137 was the live total; 22,115 unique records came back across
222 pages. The 22 missing are churn during the pass (people who left the network
between page 1 and page 222), not a pagination fault.

## The 199 is a floor, not the real number

HeyReach returns `headline: null` for every one of the 22,115 records, and `about`
for only 3,859 of them (17%). So "is this a cross-border business" could only be
read off the **company name**. A company called Galera Fresh passes. Tetakawi,
which moved $1.7B across the Mexican border, does not — nothing in the name says so.

That means the name test undercounts badly. The earlier hand-inspected 300-person
sample put the real both-tests rate at 5.0%, which on 22,115 is roughly 1,100, and
about a third of those failed on inspection. So:

- **199 people are qualified and actionable today**, no enrichment needed.
- **Roughly 450 to 700 is still the honest estimate of the real pool**, and getting
  from 199 to that number means enriching the 5,771 decision seats by company
  against Apollo or ZoomInfo. That is a separate job, not a bigger LinkedIn pull.

The full pass did not overturn the estimate from the sample. It confirmed it and
handed over the part that can be worked without further research.

## Breakdown of the 199

| sector | count | of which finance seat |
|---|---|---|
| produce / fresh | 47 | 5 |
| logistics / freight | 41 | 6 |
| food / protein | 22 | 4 |
| wine / spirits | 14 | 1 |
| import / manufacturing | 4 | 1 |
| other, matched on bio text | 71 | 20 |

Ranked produce and fresh first, because every conversion this month came from there.
Full list: `data/fx/linkedin/first-degree-qualified-2026-09-25.csv`.

## Collisions caught before the list was handed over

Three people were dropped because their company is already being worked. One seat
per company.

- **Christian Vega, VP, Galera Fresh** — Erica Vega, COO, messaged 2026-09-23. Third
  Galera seat to surface after Paco Jr and Pepe Vega. The company is spelled
  "Galera Fresh" in the network and "Galera Fresh Produce" in the pipeline, so an
  exact-string check would have missed it.
- **José Bernal, Sweet Seasons LLC** — Marina Bernal replied "not interested"
  2026-09-06. Same surname, same company. Do not go back in through a relative.
- **Ivan Petrov, Safer Food Services** — Humberto Martinez, awaiting reply since
  2026-01-07.

## Known false positives still sitting in the 199

Left in the file rather than silently deleted, so the judgment stays visible:

- **Eric Deudney, Southall - Farm and Inn** — a Tennessee resort. "Farm" in the name.
- **Cathy Burns, International Fresh Produce Association**, **Steven Callaham,
  Dundee Citrus Growers Association**, **Manuel Michel, Colombia Avocado Board**,
  **Alvaro Luque, Avocados From Mexico** — trade bodies and marketing boards. They
  buy nothing in foreign currency. Worth knowing, not worth a Play 0 invitation.
- **Willian Valiante, EY** — consulting, matched on his own bio text.
- **Humberto Salazar, Fresh Express** — not a false positive, but he is already in
  the Play 0 batch 4 queue. Do not add him twice.

## Cost to work it

First-degree connections take a direct message, which does not consume the daily
invitation quota. At roughly 30 messages a day the 199 is about a week; the estimated
450 to 700 is about a month. Either way the invitation budget stays free for the
cold plays.

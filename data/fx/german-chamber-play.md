# German-American Chamber play: paused, waiting on the member roster

Marcel, 2026-09-25: *"no stop for now for german companies i will try to get the
list of german companies from the german chamber"*.

**This is the better route** and the build was stopped on it. A real GACC South
member roster beats inferring the population from LinkedIn company names and
contact databases, which is what was underway.

## Where the thesis came from

Jason Roof, Monex USA, on the 2026-09-25 call: he speaks German fluently, is
deeply involved in the German-American Chamber of Commerce **GACC South** (Texas
up through DC and down to Florida), and **Monex is already a corporate member**,
so attending costs no budget ask. His thesis, in his words: *"many of the German
subsidiaries here have operations in Mexico and Brazil. So it's more than just
US dollars to euros. Maybe dollars to Mexican pesos, reais as well."*

That is the referral engine between the two desks. Jason brings the German
parent relationship and the language; Marcel brings Mexico, Brazil, Portuguese
and Spanish. He also asked Marcel to send him German-community companies as they
surface.

## What the partial scan found, and why the network alone was not enough

Scanned all 22,115 first-degree records for German, Austrian and Swiss markers:
corporate suffixes (GmbH, AG, KG, SE), roughly 150 named DACH industrial groups,
and DACH place names in the company field.

| | count |
|---|---|
| Records with a DACH marker | 196 |
| Obvious false positives dropped | 40 |
| **US located** | **24** |
| **Mexico located** | **84** |
| Elsewhere or unknown | 48 |
| **In Texas** | **4** |

**The geography is the wrong way round for this play.** The bulk of Marcel's
DACH network is the *Mexican* side of these groups: Audi México, Bosch México,
Leoni México, ZF Suspension Guadalajara, Evonik de México, Holcim México,
Volkswagen Financial Services México, GEA Internacional. Those are exactly the
seats the Mexico decision-seat test exists to filter, because a German group's
Mexican subsidiary banks where group treasury says.

The four Texas names are LyondellBasell (Francisco Morgadinho, VP Finance and
Strategy, Houston), EagleBurgmann (Nelson Peixoto, VP Finance and Controlling
Americas, Greater Houston, **already in the pipeline**), Heidelberg Materials
(Bob Shori, VP Program Management, Irving) and Continental Battery Systems
(Ariba Shibli, Assistant Accountant, Dallas).

False positives worth knowing about, because they will recur in any keyword
scan: **Arca Continental** is a Mexican Coca-Cola bottler, not Continental AG,
and it was the single largest hit at 14 records. Also Colegio Continental,
Bavaria-Colombia, and Novartis, Roche and Zurich Insurance, which are Swiss but
neither industrial nor the right size.

Full scan output, kept for when the roster arrives:
`data/fx/linkedin/dach-network-scan-2026-09-25.json`.

## The objection this play will meet, learned the same day

**Rohlig Logistics, Richard Labib, CFO NORAM region at Rohlig USA.** German
freight forwarder, Bremen, founded 1852. Marcel wrote on 2026-09-24 and Labib
answered about 21 hours later:

> Hi Marcel, thanks for reaching out. We use cashpooling and aren't in the
> market.

The first German-owned company to answer said **the treasury decision is not
local**. Cash pooling is what German groups run, and netting intragroup flows
centrally is precisely what removes a local CFO's reason to talk to a provider.

So the German play needs an answer to cash pooling before it scales, not after.
Two lines worth testing when it resumes:

1. **Cash pooling nets intragroup flows. It does not price third party
   conversion.** Agent settlements, local supplier payments and payroll in a
   third currency can sit outside the pool.
2. **Go where the pool does not reach.** A German parent's *Brazilian or
   Mexican* operating payments are often funded locally rather than swept, which
   is the part of Jason's thesis that actually creates a US-side decision.

Neither is proven. Both are hypotheses to put to Jason, who ran a currency
hedging automation business at Kantox and will know immediately which holds.

## What happens when the roster arrives

The hard part, who the companies are, will be solved. The work then is fast:

1. Screen the roster against `pipeline.json` for collisions, company level as
   well as person level. One seat per company.
2. Find the decision seat at each, favoring the US entity's CFO or controller
   over the parent.
3. Separate the ones with Mexican or Brazilian operations, which is the whole
   point of the play and Marcel's edge over any other Monex seat.
4. Sort out which are too big and already run group treasury, applying what
   Rohlig just taught, before writing to anyone.
5. Hand Jason the list he asked for, rather than a pitch.

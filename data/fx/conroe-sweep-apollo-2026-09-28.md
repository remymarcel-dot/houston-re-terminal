# Conroe sweep, run properly, 2026-09-28

Marcel: *"run the conroe sweep with headcount 11-200 and industry filter"*.

## How it was run, since it was not LinkedIn

LinkedIn search is not reachable from here and HeyReach exposes no import from
search URL. **Apollo was used instead**, which carries the exact filters asked for.
This spends Apollo credits from Marcel's account. The response carried no
`mcp_credits` block, so the exact cost cannot be stated; Apollo documents one
credit per successful search on the company endpoint.

Filters applied:

- person location: Conroe, Texas
- employer headcount: **11 to 50 and 51 to 200**
- employer NAICS: **31, 32, 33** (manufacturing), **42** (wholesale trade),
  **48, 49** (transportation and warehousing)
- titles: CFO, Controller, VP Finance, Finance Director, Owner, President, Treasurer

## Result: 213 matches

Against roughly a dozen profiles worked by hand all evening, for two keepers.

## The filter validated itself

Three names already worked tonight came back in the first page, which is the best
evidence the filter is aimed correctly:

- **Paul Miller, CFO, Deveraux Specialties** — ranked second. Already in
  Wednesday's wave 625896.
- **Joshua Eaton, Controller, TURBINE-X Energy** — was parked as "cannot screen
  without more".
- **Jessica Echegaray, CFO** — and it answers the open question: her employer is
  **Pyxis Lab Inc**. Her LinkedIn profile enriched with a null company earlier
  today.

## Standouts on the first page, by visible FX thesis

| Seat | Company | Why |
|---|---|---|
| VP Finance | **Tongrun International** | Tongrun is a Chinese manufacturer; a US arm is an import book by construction |
| Controller | **Tex-Isle, Inc.** | Pipe and OCTG distribution, a trade that runs on imported steel |
| Controller | **Curtis Steel Company** | Steel distribution |
| President/Owner | **Southern Fab & Supports, a subsidiary of LISEGA Inc.** | LISEGA is **German**. Foreign parent, US operating company |
| VP Finance / Controller | **GPS Paints LLC** | Coatings manufacture, imported raw materials |
| Owner and President | **Decor Builders Hardware** | Hardware distribution |
| Financial Controller | **6th Sense Fishing** | Tackle, an almost entirely imported category |
| Owner | **Kimjbo Distributors** | Distribution |
| CFO and Owner | **Advanced Freight Dynamics LLC** | Freight, and both seats are in the list |

## Two real problems before any of this can be worked

**1. Last names are masked.** Apollo returns `Ru***o`, `Mi***r`, `Ol***r`. The
plan obfuscates them in search results. Revealing them needs People Enrichment,
which costs credits per person.

**2. Apollo returns no LinkedIn profile URL in search.** The entire pipeline runs
on LinkedIn URLs, so nothing here can reach HeyReach without enrichment either.
Enrichment does return `linkedin_url`.

So the sweep proves the filter and produces a target list, but converting it into
sendable leads is a second, paid step. **Not taken without Marcel's word.**

## Also worth flagging: the geography filter leaks

Several results are plainly not Conroe: Eurofast Poland, BELBO Sugheri in Italy,
ETSE ET in Turkey, Negin Mokran Petrochemical in Iran, Perla Harghitei in Romania,
TECHNOGENIA in France, and SEEKING TRADE & LOGISTIC S.A. de C.V. in Mexico. Either
Apollo matched the place name loosely, or those people really do list Conroe while
working for foreign employers. Both are possible and the difference matters,
because the Mexican entity would trip Marcel's rule. **Any list built from this
must be re-checked on location before anything is sent.**

---

# Top 20 enriched, 2026-09-28

Marcel: *"TOP 20"*, after interrupting his own *"300"*.

**Cost: 20 Apollo credits, exactly 1 per person**, across two calls of ten. No
phone or personal email reveals were requested, which keeps it to the standard
match rate. Enrichment returned full names, **LinkedIn profile URLs**, work emails,
full employment history and company detail.

Selection rule applied before spending: one seat per company, finance or owner
seats only (the search had pulled in Production, Process, Quality and Project
Controllers, which are operations roles), and no foreign-domiciled employers.

## Tier 1, worth an invitation

| Seat | Company | The thesis |
|---|---|---|
| **Joseph Rangel, CPA**, Controller<br>`linkedin.com/in/josephrangelcpa` | **Tex-Isle, Inc.**, Conroe. 1959, 96 staff, $17.6M | API line pipe and OCTG. Steel pipe distribution runs on imported product. He was **Financial Controller, Completions, Worldwide at Smith International** and a Schlumberger controller, so multi-currency is not new to him |
| **Heather Olivier**, Controller<br>`linkedin.com/in/heather-olivier-49092b14` | **Curtis Steel Company**, Conroe. 1976, 90 staff | Flat-rolled steel service centre: galvanized, galvalume, cold rolled. Imported coil is the norm in that trade |
| **Chris Grappe**, President<br>`linkedin.com/in/chris-grappe-a8180b35a` | **Southern Fab & Supports, a subsidiary of LISEGA Inc.**, Conroe. 15 staff | **German parent.** Fifteen people under a German pipe-support group. Small enough that the president signs |
| **Marcia Rubio**, VP Finance and Controller<br>`linkedin.com/in/marcia-rubio-69682a5a` | **GPS Paints LLC / GPS Coatings — GRUPO SAYER**, Conroe. 22 staff | **Mexican parent.** Grupo Sayer is a Mexican coatings group and she has been with it since 1998. US LLC, so the same clean structure as Elementia USA. Spanish note |
| **Alana Lyons**, CFO<br>`linkedin.com/in/alanalyons` | **Advanced Freight Dynamics LLC**, Conroe. 26 staff | Heavy haul and project logistics, and its own keywords include **international freight, international shipping, international oversize shipping**. CFO seat at 26 people |
| **Robbi Turek**, Owner<br>`linkedin.com/in/robbi-turek-06052115` | **Decor Builders Hardware, Inc.**, Conroe. 1972, 55 staff, **$41M** | Decorative, architectural and cabinet hardware. That category is imported almost by definition. Owner seat on $41M of revenue |
| **William White**, VP Finance<br>`linkedin.com/in/william-whiteb` | **Tongrun International**. 2012, 71 staff | Contract manufacturing: sheet metal, die-cast, injection moulding, casting. The name is a Chinese manufacturing group. Ex NOV, Trican, Robbins & Myers. **Note: Bonham, Texas, not Conroe** |
| **Mike Sorna**, Owner<br>`linkedin.com/in/mike-sorna-41461132` | **NovoSci Healthcare**, Conroe. 21 staff | Custom OEM surgical components and perfusion kits, keywords include **global distribution**. Owner seat |

## Tier 2, plausible, held

- **Joshua Eaton**, Controller, **TURBINE-X Energy**, `linkedin.com/in/joshua-eaton-cpa-61816713`. He sits in Conroe; the company is headquartered in **Nisku, Alberta, Canada**. A Canadian parent means a real CAD relationship, and Canada is in scope under the rule Marcel set on 2026-09-25. This one may belong in Tier 1 on a second look.
- **Joshua Eminhizer**, Controller, **6th Sense Fishing**, Willis TX, 39 staff. Tackle is an import-heavy category, but the company's own keywords say "crafted in USA", which cuts against it.
- **Linda Anderson**, Owner and CEO/CFO, **Ergo-Flex Technologies**, Conroe, 18 staff, **$36.8M**. Medical devices. Thirty-seven million dollars across eighteen people is a striking ratio and worth understanding, but no international signal appears anywhere in the record.

## Cut, with the reason

- **Logan Badger** — the one outright bust. Enrichment shows him as "Distributor at LBsimplebizABC1" and owner of "Do It Yourself Small Houses", while Kimjbo Distributors is health and wellness in **Bartlett, Illinois**. The search row was misleading and the credit was wasted.
- **Dan Ries**, CFO, Wagner Machine — he is in Conroe but the company is in **Norton, Ohio** and its own keyword is "made in ohio". A domestic CNC job shop.
- **Christi Sandel**, CFO, KBK Industries — Rush Center, **Kansas**. Fibreglass and poly tanks, domestic.
- **Mary Lechuga**, Controller, K&K Supply — Fenton, **Missouri**. Construction supply, domestic.
- **Adam Harwell**, CFO, Clean Chemistry — Longmont, **Colorado**, $120M. Domestic and larger.
- **Vanessa Shields** (Rowmec, 11 staff), **Jordan Holley** (Royal Equipment, 29 staff), **Tim Van Roekel** (Knight Energy, 130 staff) — all Texas, all domestic, no international signal in the record.
- **Jessica Echegaray**, CFO, **Pyxis Lab**, Tomball. Industrial water-chemistry instruments, no international signal. The enrichment did at least answer the question LinkedIn could not: this is the employer that came back null earlier today.

## What this says about the two methods

| | Profiles looked at | Worth contacting |
|---|---|---|
| LinkedIn, link by link, all evening | ~12 | 2 |
| Apollo, one filtered sweep | 20 | **8, plus 3 held** |

Same person, same judgement, same evening. The difference is the filter.

**Nothing built. Nothing sent.** Wednesday's wave already holds seven, so adding
eight would put fifteen invitations on one day, which is the ceiling exactly. A
Thursday wave is the right home for these.

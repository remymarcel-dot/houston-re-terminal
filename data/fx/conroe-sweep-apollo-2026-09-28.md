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

# Ideal customer profile

## Qualifies

**Titles** — CFO, Treasurer, VP/Director of Finance, Controller, Finance
Manager, Head of Treasury. Also CEO or Owner at companies small enough
that they run their own banking (roughly under 200 people).

Titles containing "Americas", "LATAM", "International" or "Global" are
strong signals: the person likely owns a multi-currency P&L.

**Trade-exposed sectors**

- Manufacturing, especially with Mexico operations (nearshoring)
- Automotive, aerospace, electronics and medical device suppliers
- Agriculture and produce — growers, packers, exporters
- Logistics, freight forwarding, customs brokerage
- Energy services and oilfield equipment
- Consumer goods importers and distributors
- Construction materials and industrial equipment

**Geography**, in priority order

1. Houston and Texas metro — his home market, meetings are easy
2. Border and nearshoring corridors — El Paso/Juárez, Laredo, Eagle Pass,
   San Antonio, Monterrey
3. US-wide with genuine cross-border flows
4. Mexico, Brazil and LATAM where the US entity does the paying

**Buying signals**

- Foreign parent company (intercompany settlement in EUR, JPY, KRW)
- A US subsidiary being stood up, or a new North American hub
- Suppliers or customers named in non-USD countries
- Import/export language anywhere in the profile or company page
- Recent expansion, new plant, or a funding event

## Does not qualify

Disqualify on sight and never draft to:

- **Anyone selling to Marcel** — staffing and IT outsourcing, event
  sponsorship sales, SaaS BDRs, freight brokers pitching TMS, sales
  trainers, recruiters. His inbox is full of these and they are noise.
- **Competitors** — bank FX desks, other payment providers, brokers
- **Pure-domestic businesses** with no plausible currency flow
- **Students, job seekers, consultants** with no company behind them
- **Anyone already a Monex USA client** — check pipeline first
- **Anyone who has opted out**, permanently
- **Anyone not currently in the seat.** A person between roles has no
  payments to move and pitching them reads as tone-deaf.

## Product eligibility — check before offering anything

The two products have different eligibility, and offering the wrong one
promises something Marcel cannot deliver.

| Product | Who can actually buy it |
|---|---|
| FX and cross-border payments | Any company with non-USD flows, subject to the US-companies focus |
| **Receivables factoring** | **US-based companies only** |

**Factoring is US-only.** A foreign supplier, plant or subsidiary cannot
be advanced against its invoices, even when its buyers are US companies
and even when the group has a US arm. The entity being financed is what
must be US-based.

So on a multi-country relationship, split it properly: factoring is for
the US entity's own receivables, and the foreign side of the supply
chain is an FX and payments conversation, never a financing one.

Worked example: Scarpa Worldwide (Delray Beach) sources from Ecuadorian
processing plants. Factoring can be offered to Scarpa, not to the
plants. The plants are out of scope entirely.

Also note Ecuador is dollarized. Paying an Ecuadorian supplier in USD
involves no conversion, so there is no FX story there either — the FX
lives wherever the non-USD currencies actually are, which for Scarpa is
India sourcing and any European or Asian customers settling in their own
currency. Do not manufacture an FX angle for a dollarized country.

## Check whether they are actually in the seat

HeyReach's `position` and `companyName` are scraped and go stale. Someone
who left a CFO job six months ago still shows as its CFO. Before treating
a senior title as a live lead, look for transition signals:

- "Aspiring Board Member", "Advisor", "Open to Work", "Fractional",
  "Ex-", or a headline that reads as a career summary rather than a job
- The company was acquired, taken private, or wound down
- Marcel's own earlier messages in the thread — if he wrote something
  like "as you look at your next seat", he already knew

Someone in transition is **not a lead, and not noise either**. They are a
peer relationship worth keeping warm: they will land somewhere that may
have currency exposure, and Marcel is himself open to country manager and
commercial leadership roles, so the value runs both ways. Reply to them
as a peer, with no pitch in it at all, and log them as
`outcome: "relationship"` rather than dropping them.

Worked example: Daniel O'Quinn showed as "CFO, SciPlay" but SciPlay had
been taken private, his headline ended "Aspiring Board Member", and
Marcel's own opener said "as you look at your next seat". Lead on paper,
peer in reality.

## Segmentation in practice

`get_my_network_for_sender` returns `position`, `companyName`,
`location` and `headline`. Filter on those. Roughly:

1. Pull network pages (`pageSize` 100) and filter by title keywords
2. Within those, filter by sector and geography signals
3. Drop anyone already in `pipeline.json` or with an open conversation
4. Rank: Houston/Texas first, then foreign-parent, then title seniority
5. Take the top 15-20 for the cycle

A large chunk of the 21,778 have null `position` and `companyName` —
those are unusable without enrichment. Skip them rather than guessing.

## What actually makes a lead

A person is a lead when they have confirmed, in their own words, that
their company moves money in a currency other than USD. Everything
before that is a target. Log the distinction in `pipeline.json` so the
weekly numbers mean something.

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

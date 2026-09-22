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
- **Venezuela, in any form.** See the hard stop below.

## Venezuela is a hard stop, not a judgement call

Marcel, 2026-09-22: *"venezuela is forbidden we can nt touch"*.

This is not a preference to weigh against a good lead. It is a rule with
no exceptions and no clever workarounds. Disqualify on sight:

- A company operating in Venezuela, entering it, or re-entering it
- A person whose seat names Venezuela, even as one country among several
  (a "CFO, Central America, Caribbean and Venezuela" is out)
- A consultant or advisor whose practice is Venezuela entry
- Any flow whose counterparty sits in Venezuela

**The workaround that does not work.** Venezuela-bound activity usually
routes through Panama or Colombia in practice, and both of those
corridors are ones Monex genuinely covers. It is therefore tempting to
offer the Panama or Colombia leg and call it a different transaction. It
is not a different transaction. The counterparty behind it is still
Venezuelan and the sanctions exposure travels with the flow, not with the
country code on the payment. Never propose this, in a draft or in a
conversation.

This was drafted once, on 2026-09-22, to J Mears Consulting, Jesus Mears,
whose whole practice is Venezuela entry advisory. Marcel caught it before
it sent. The reasoning that produced it was that he looked like a channel
rather than a prospect, which was true and entirely beside the point: a
channel into a forbidden market is still the forbidden market.

**When Venezuela appears in a live thread**, do not pivot, do not offer an
adjacent corridor, and do not keep the relationship warm for later. Close
it out courteously on a human note with nothing offered, and mark the
contact do not contact.

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

Second worked example, and a warning about the limits of this screen:
Steven Wojtowicz showed as "N.A. Treasury Director, Ferrero USA" and
passed every filter. He had retired eight months earlier. LinkedIn still
carried the old title and `get_my_network_for_sender` returns `headline`
as null, so there was nothing in the data to catch it. Expect roughly
one stale record in twenty five from network pulls, accept that the
screen cannot catch them all, and never present the screen as complete.

**Do not trust HeyReach's auto-tags.** It labelled that reply "Not
interested". He had not declined anything, he had left the job. Read the
reply itself and let it override the tag.

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

## Do not cut the network by connection date

A segmentation run screened to connections made in 2025 or later, on the
reasoning that everything older belonged to the Seidor and SAP years and
was stale for FX work. That was wrong and it hid live prospects.

Measured against the archive: **160 people connected before 2025 hold
decision maker titles and have been in conversation since 2025, and 66 of
them have replied at least once.** These are the older Mexico and LATAM
relationships, and they answer at a far better rate than anyone cold,
because the relationship predates the pitch.

Safer Food Services (SFS US), Humberto Martinez is the proof. Connected in
June 2019, agreed to a meeting twice in February 2026, gave his corporate
email, and never appeared on any target list because of the date cut.

Screen on the title, the company and whether there is real FX exposure.
Connection date says when Marcel met someone, not whether they are worth
talking to. The Hashtag_Follows export is stale; the people are not.

## Screen for size before drafting a reopen

GOB ENERGY SOLUTIONS LLC, Logun Roberts sent the strongest signal in the
whole archive, an outright "Can you call me please sir" with his number,
and Marcel closed it as too small to work.

Signal strength tells you someone will take the call. It says nothing
about whether the account is worth the hour. Screen size and real currency
exposure before writing a reopen, not after, or the strongest looking rows
on any list will keep being the ones that waste the most time.

Company size is not in the LinkedIn export, so where a name is unfamiliar
and the company is small or unknown, ask Marcel before drafting rather
than assuming a loud signal means a real account.

## Qualify before presenting, not after

Three of the first nine "explicit yes" rows failed basic qualification the
moment Marcel looked at them:

| | why it should never have been shown |
|---|---|
| GOB ENERGY SOLUTIONS LLC | too small to work |
| AUSY Engineering | already a customer, onboarded in August |
| Xefco | Australian, and very small |

Xefco is the worst of the three. US companies only has been a standing
directive from the start, and an Australian company reached the list
anyway, because the screen read titles and sector words and never checked
where the company is.

The LinkedIn export carries no country and no size, so those have to come
from somewhere else before a name is put in front of Marcel:

1. Apollo's free `organizations_lookup` resolves the domain, which often
   settles the country on its own (a .mx or .es domain, or an obvious
   local brand).
2. A web search settles size and footprint for anything unfamiliar.
3. Where both are still unclear, ask Marcel in one line rather than
   drafting. He knows these companies in seconds.

A strong signal is a reason to qualify a company, never a substitute for
qualifying it.

## The test is where the buying decision sits, not whether a US entity exists

Grupo Industrial Saltillo was put forward as the strongest name in the warm
set: roughly a billion dollars of revenue, listed, US subsidiaries, a real
currency book. Marcel killed it in one line. It is a Mexican company.

US subsidiaries were not enough, and that is the whole lesson. A Mexican
listed group's CFO sits in Mexico and banks in Mexico. That relationship
belongs to **Monex Mexico**, not Monex USA, which is a separate US licensed
entity. Chasing it is not just out of scope, it is reaching across a
colleague's desk.

Compare with Grupo Palco, which Marcel did approve. Also Mexican
headquartered, but the contact was engaging about a US event, the group
runs operating US entities in El Paso, and the flows being discussed
settle on the US side.

So ask where the decision and the banking sit:

| | verdict |
|---|---|
| US company, US treasury | yes |
| Mexican group with US operating entities, US side flows, US contact | worth checking with Marcel |
| Mexican parent, CFO in Mexico, group treasury in Mexico | no, that is Monex Mexico's |

Revenue size does not override this. A billion dollar Mexican corporate is
a worse target for Marcel than a twenty million dollar Texas importer.

## Cheap country tells already in the data

Country is not a field in the LinkedIn export, but it is often sitting in
plain sight in the thread itself. Screen on these before anything else:

- **A +52 mobile, or any non US country code**, offered as the contact
  route. NETCURIO, Pablo Sedano gave a +52 cell and asked for WhatsApp,
  which was the answer before any research started.
- **A .mx, .es or other country domain** on the email they hand over.
- **The language and register of their own messages**, especially Mexican
  business Spanish with no US context anywhere in the thread.
- **Company suffixes**: S.A. de C.V., S.A.B., S. de R.L., Ltda.
- **A US area code** is the positive version of the same tell.

None of this is conclusive on its own, but each one is free and catches
most of what the title based screen lets through. Apply it before spending
a search, and certainly before putting a name in front of Marcel.

## An English company name proves nothing about country

"The Cash flow Doctor" reads American and is a Mexico business. Marcel
closed it on the same test as Grupo Industrial Saltillo and NETCURIO.

Three of the nine explicit-yes rows died on country alone, and in each case
the company name pointed the wrong way or nowhere at all. Never infer
country from the name. Use the tells in the thread, the domain, or ask.

### Scoreboard for the explicit-yes exercise

Nine rows surfaced, and Marcel killed them one at a time:

| reason | count |
|---|---|
| Mexican business, belongs to Monex Mexico | 3 |
| too small or not worth the time | 2 |
| already a customer | 1 |
| out of country entirely (Australia) | 1 |
| the yes was about something else | 1 |
| still open | 1 |

The lesson is not that the detector was badly built. It is that **signal
detection without qualification produces work for Marcel rather than
leads.** Country, size and customer status decide almost everything, none
of the three is in the LinkedIn export, and all three must be resolved
before a name is shown to him.

## "CFO Mexico" is not automatically disqualifying

Two seats with almost the same title landed on opposite sides of the test.

**Cut:** Nexteer, Rogelio Villa, "Chief Financial Officer - Mexico". Sits
in Mexico, at a global automotive group that runs its own treasury.

**Kept:** Jones Plastic & Engineering LLC, Luis Reynoso, "CFO - Mexican
Operations". Sits in **El Paso, Texas**, at a mid size US LLC.

Luis is the better target than most plain US CFOs on the list, because the
dollars sit on his side of the border, the pesos are his actual remit, and
the decision is his to make. A title mentioning Mexico can mean the person
runs Mexico from Mexico, or that they run the Mexican exposure from the US
side. Those are opposite prospects.

Read **where the person is** and **what the company is**, never the job
title alone.

## A CFO in their first six months is the best timing signal available

SMTC Corporation, Sravan Sura became CFO in August 2026. Two months in.

Most prospects have no reason to change anything: the bank relationship
works, the spread is invisible, and switching costs attention nobody has.
A new CFO is the exception. They are explicitly reviewing what the
business pays for, they carry no loyalty to decisions they did not make,
and they are expected to find something.

Look for it on every profile. A start date inside the last six months on a
finance seat changes the opener from "here is a cost you have" to "you are
already looking for these".

Stronger still when the background is private equity, as his is, Apollo
and H.I.G. A PE trained CFO is hired to find margin, and a spread buried
inside a bank rate is exactly the kind of cost that survives only because
nobody examined it.

Do not open on the new role as flattery. Open on what the job actually
involves right now.

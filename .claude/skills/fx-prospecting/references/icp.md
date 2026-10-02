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
4. **Canada.** Marcel, 2026-09-22: *"do not skip canadian companies we
   can also on board them"*. Monex USA onboards Canadian companies.
   A Canadian head office is **not** a reason to cut a lead, and the
   standing "US companies only" line does not extend to Canada.
5. Mexico, Brazil and LATAM where the US entity does the paying

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

## Canada is in scope, Mexico is the one to test

The country rule exists because a Mexican parent banks in Mexico and that
business belongs to Monex Mexico, not to Marcel. It was over applied on
2026-09-22 to **Vexos**, cut for having a Markham, Ontario head office.
Marcel corrected it: Canadian companies can be onboarded.

So the country screen is not "is it American". It is:

- **Mexico** — apply the decision seat test below in full
- **Canada** — in scope, no special test
- **Venezuela** — forbidden, see the hard stop above
- **Elsewhere** — the test is whether a US or Canadian entity does the
  paying

Vexos remains cut, but on size alone: 750 people, $100M to $500M, with a
CFO, an SVP of Global Supply Chain and an Asia organisation. That is the
Siemens and Bosch shelf, not the owner-signs-the-wire shelf.

### A Canadian company is onboarded by Monex USA, not handed to Monex Canada

Marcel, 2026-09-25, asked directly whether the Bondi Produce message should
sign as Monex USA when Bondi is a Toronto company and Monex Canada exists with
Andrew Barranca sitting there: *"we can on board canadian compan so with monex
usa"*.

So a Canadian prospect is Marcel's own deal, not a referral. **Write to them
exactly as to a US prospect, signing Monex USA.** Do not hedge the entity, do
not offer to pass them to a colleague, and do not raise the question in the
message. Monex Canada being a sister company is not a reason to route a lead
away from him.

The payment grammar still applies, just with Canada as the paying side rather
than the destination: the Canadian entity is the subject of the sentence and
the money points outward, the same way a US entity would. Bondi buys in euros
and sells in Canadian dollars, so the question asked was who pays the overseas
producers, not anything about the European side.

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

### A treasury title in Houston selects against the ICP, not for it

Searching Houston by treasury or senior finance title keeps returning the wrong
companies, and the reason is structural rather than bad luck.

**Only large companies employ people whose title is treasury.** A Treasury Senior,
a Treasury Analyst, a VP of Treasury exists because the company is big enough to
have a treasury department, which is the same thing as being big enough to have
bank FX lines and a group treasury policy. The title is therefore a reliable
signal that the company already has a desk.

The run of 2026-09-28 makes the point better than any argument:

| Seat searched into | Company | Why it failed |
|---|---|---|
| VP Finance, Accounting and **Treasury** | U.S. Silica | Apollo owned, 26 US facilities, domestic |
| **Treasury** Analyst | Excelerate Energy | Listed, treasury team above her |
| **Treasury** and Financial Analyst | Wellbore Integrity Solutions | PE backed carve out, analyst seat |
| CFO, US arm | ContourGlobal | KKR owned, London treasury |
| Finance and Operations | Perennial Power | Sumitomo subsidiary |
| CFO and Administrative Manager | Ecopetrol USA | Colombian state major, Bogotá treasury |
| **Treasury** Senior, CTP | Repsol | Spanish supermajor, Madrid treasury |

**The ICP has no treasury department.** A mid market importer, distributor,
forwarder or manufacturer has a CFO, a controller, or an owner who signs the wire
himself. That is precisely why Marcel's own correction holds: *"also consider
owner as smaller companies do not have a finance guy"*.

**So search the business, not the title.** Filter on industry (manufacturing,
wholesale, logistics, food and produce), on headcount (roughly 11 to 200), and on
a cross border fact about the company, then take whatever finance seat exists.
Every name that worked on 2026-09-28 came out that way: Rigaku Americas (Japanese
parent), Refined Technologies (crews worldwide), Deveraux Specialties (ingredient
importer), Pure Import Logistics (owner, origin agents), Javid (shelter payroll in
pesos), Federated Maritime (dollar revenue, foreign port costs).

## Ask, do not assume

Marcel, 2026-09-30, on Jamie LaChapelle at CDS Distributing:
*"we should ask not assume"*.

When a profile establishes the seat but leaves the currency question open,
the opener asks the question. It does not invent an answer that sounds
plausible. Two different reasons, both of which cost real money:

1. **Guessing wrong in front of someone who knows** is the fastest way to
   be dismissed. A produce distributor who buys landed from importers
   knows perfectly well that he has no FX exposure, and a note asserting
   that he does proves the sender did no work. To a first degree
   connection it reads worse still.
2. **A question is easier to answer than a claim is to correct.** "Does
   CDS buy direct from the growers or landed from importers" takes one
   line to answer and starts a conversation. "Your grower payments move
   with the rate" forces the reader either to agree with a stranger's
   guess or to write a correction, and most people do neither.

Worked examples, all of them Marcel's own instinct rather than a rule
applied afterwards:

- **Gustavo Elias Hopkins, IPR Fresh:** "una pregunta corta y nada más: en
  IPR Fresh, ¿quién lleva los pagos al lado mexicano?"
- **Oscar Espinosa, Intercast:** the opener asks who owns the McAllen
  entity's payments rather than assuming the general manager in Reynosa
  does.
- **Ricardo Yllescas, Elementia USA:** asks whether the FX decision sits in
  Houston or with group treasury in Mexico City, and offers a real out.
- **Stefan Lazaridis, Proximo Spirits:** asks whether the peso book sits at
  the US company or upstream at Becle.

The pattern in all four: name the fact that is verifiable from the profile,
then ask the one thing that is not. Offering a genuine out ("if it is not
your area, no problem") is what makes the question land as respect rather
than as a qualifying script.

**Where this does not apply.** When the profile itself states the flow, say
so plainly instead of asking a question whose answer is already on screen.
Asking Nathan Boardman whether he pays people in Trinidad, Guyana and
Suriname when his own banner names all three would read as not having
looked.

## Apply the size test to the seat, not to the parent company

Corrected 2026-09-30, after Marcel overruled a cut of Pablo Ortiz Rodea,
CFO North Cone at WPP Media.

"Large company therefore a bank desk already owns this" is a good filter
and it is applied wrongly when it is applied to the logo. What the rule is
really about is whether **this person's payments** are run by a central
treasury. Two different cases hide behind the same headcount:

- **The seat IS the central function.** A corporate Treasurer at GXO, a
  Global Controller at HUB International, a Deputy CFO at GroupM. Their job
  is the desk, so they already have the bank lines. Cut stands.
- **The seat runs a market or a region.** A regional CFO covering Miami,
  Puerto Rico and Central America buys media in quetzales, lempiras,
  colones and cordobas and bills clients in dollars. London does not sit on
  every one of those payments, and large groups give their LATAM markets
  real autonomy. **That is a live payables book regardless of the parent's
  revenue.**

So before cutting on size, ask what the person actually settles. A regional
or country CFO, a divisional CFO, or a US subsidiary CFO of a foreign
parent can all be in scope at a company far above the band. What is out of
scope is the group treasury function itself.

The related trap runs the other way too. A person whose title contains
"Treasury" at a company **small** enough to lack a treasury department is
usually mislabelled, and a person whose title lacks it at a company large
enough to have one may still control a real regional book.

## A new role announcement is a real trigger, and congratulating is the wrong opener

A CFO or controller who has just started is one of the best windows there
is: they inherit arrangements they did not choose and audit them in the
first six to twelve months. They are also unusually active on LinkedIn in
those weeks and accept connection requests at a much higher rate.

**So send early, and do not lead with congratulations.** In the days after
an announcement their inbox fills with them, and a large share come from
vendors using the congratulation as a wrapper for a pitch. Opening that way
puts Marcel in the same bucket as everyone else and a finance executive
recognises the pattern instantly.

The opener that works acknowledges the new seat by being **useful about it**
rather than by celebrating it. Marie Engels at Avania, 2026-09-30, one day
after her announcement:

> "Marie, one month into a CFO seat is when you inherit arrangements nobody
> explains, and at a CRO running trials across three continents the currency
> ones tend to be buried. Not a pitch, just worth knowing who to call when
> you reach it."

Note what it does not do. It asks her nothing, because someone in week five
may not yet know how the treasury is structured, and asking puts her on the
spot. It assumes she has a list, accepts she is not on this item, and offers
to be there when she gets to it.

**The distinction that decides the verdict on a brand new hire.** A new
**CFO** has authority from day one and is worth approaching immediately. A
new **Controller** or manager does not yet, and is not. Zachary Robarge,
brand new Controller at a domestic Ohio distributor, was cut in the same
batch Engels was added in.

## Small logistics and transportation is a deliberate exception to the band floor

Marcel, 2026-09-30: *"i like small in logisctis and transportatioin so
outreach him anyway and any other we see."*

Said after the screen recommended passing on Go Freight, a thirteen person
Miami freight company likely below the $10M band floor, on the grounds that
it was too small and the seat supplied was an accounting manager rather than
the owner.

**He is right and the reasoning generalises.** In freight and transport
specifically:

- **The band floor does not apply.** A fifteen person forwarder paying a
  foreign agent every week has a real recurring flow even at $8M of revenue.
  Volume of payments matters more than revenue.
- **An accounting manager at a fifteen person company is not the same seat
  as an accounting manager at a five hundred person company.** At that size
  the person doing the books usually executes the wires, sees the rate, and
  can put a provider in front of the owner. Same logic that upgraded Mary
  Paz Varela.
- **There is no treasury desk to displace**, which is the single biggest
  obstacle at the top of the band. A small forwarder is a greenfield sale
  where a $639M carrier is a displacement sale.
- **The owner is one conversation away**, not four.

**What still has to be true.** The company must actually move something
across a border. Domestic drayage and domestic brokerage have no currency
flow no matter how small or how well run. When the profile does not prove
it, the opener asks, as with Go Freight: "curious whether Go Freight moves
anything internationally, or whether the book is all domestic."

So the screen keeps rejecting small logistics companies **with no
international lane**, and stops rejecting them **for being small**.

## A Mexican company with a US entity is in scope

Marcel, 2026-09-30: *"ia mexican company has a us entity i can work with
them"*.

This refines the "US companies only" line rather than contradicting it. **The
test is which entity does the paying, not where the parent is registered.**
A US LLC, Inc or subsidiary that settles its own suppliers and payroll is a
US company for this purpose, whoever owns it.

Worked examples already in the pipeline:
- **Elementia USA**, Houston, under a Mexican listed parent. Ricardo Yllescas
  is its CFO and was messaged on 2026-09-30.
- **ABA Cargo LLC**, a US LLC whose company record shows a Mexico City
  address and a +52 phone, with its **CFO sitting in Laredo, Texas**.
- **Prominox USA**, flagged on the El Paso list precisely because "USA in the
  name suggests a US entity".
- **GCC Supply & Trading**, the US trading arm of Grupo Cementos de
  Chihuahua.

**What is still out:** a Mexican entity with no US arm at all, where every
payment is made in Mexico by a Mexican company. Those were correctly cut from
the El Paso directory: Industrias CCJ de Juarez, CENALTEC, Coplasco,
Coprofusa, Miscelec, Montilla, Mrack, LA FE, Veyher Metales, VISIMAQ and the
rest.

**Where the screen has been too blunt.** Cutting a whole list on the parent's
nationality is faster than checking for a US arm, and it has probably lost
some good names. When a Mexican company appears with **USA, Inc, LLC or Corp**
in its name, or with a person in a US city holding the finance seat, check for
the US entity before cutting.

**Note the asymmetry with factoring**, which is unchanged. FX and payments
follow the paying entity. **Receivables factoring is US entity only and always
was**, so a Mexican parent can never be factored even when its US arm can.


## Check the client list before anything else

**2026-10-02, Tecma.** Gabriela Garcia, VP Finance, was screened, enriched with
ZoomInfo credits, written to, and asked whether anyone had recently shown her
the spread on her conversions. She replied that Tecma already works with Monex
for its currency trade into Mexico, that it has been a very good partnership,
and that they value the continuous support.

She was gracious. She was not obliged to be. A less generous reader would have
forwarded that email to their relationship manager with one line above it.

**So the first filter on any name is not the ICP, the seat, or the exposure. It
is whether Monex already serves them.** That check costs nothing and belongs
above enrichment, because every step after it spends money or credibility.

Two things follow when the answer is yes:

- **Stop the cadence immediately**, with `stopReason: client`. A follow-up pitch
  to a happy customer undoes the goodwill the reply contained.
- **Re-read the account as a channel.** Tecma turned out to be a shelter
  operator with 90+ cross border manufacturing clients and a VP of Finance who
  volunteers that Monex has been good to them. That is worth more than the
  meeting the original email asked for, and it is built in person, never by
  email.

And before approaching any existing client in person, **find out internally who
owns the relationship.** Appearing at a colleague's client's stand unannounced
is how a win becomes a problem.


## Size shapes the note, it does not cut the name

**Marcel's correction, 2026-10-02:** *"We should not be afraid to reach multi
billion dollar treasuries."* The second time he has overruled this, after Jakks
Pacific on 10-01. Treat it as settled.

The old habit was to flag anything above roughly $500M as out of band and
recommend cutting. That reasoning was never quite right. The objection to a large
company is **not** that the argument fails there. It is that they already have
providers, a bank panel, and often a hedging programme.

But a treasurer with all three still wants a second quote, and a large recurring
flow is where basis points actually matter. **The size of the company is an
argument for the conversation, not against it.**

What size genuinely changes is **how the note is written**:

- **Concede the obvious in the first clause.** Denis Bräuer at Element Solutions
  opens with "you have a bank panel and a hedging program, so I will skip why a
  specialty chemicals group carries currency risk." Pretending a corporate
  treasurer needs the category explained guarantees silence.
- **Ask the one question that is still open.** At that scale it is almost always
  execution versus relationship: teams review the bank annually and the rates
  never, because the rates never arrive as a reviewable document.
- **Expect a longer cycle and a lower hit rate**, and do not read silence as the
  idea failing.

What still cuts a name is **the seat, not the size**: a regional book beats a
group function for reachability, and Jakks' central finance seat was the harder
ask rather than its revenue. And a genuinely domestic business with no foreign
flow is still out, however large, which is why Lindsey Thiel at a US homebuilder
was cut while Bräuer was not.


## Check what the company does before deciding it is an account

Two names sat on the 2026-10-02 worth-a-note list with the same parking note:
the warm path is excellent but the company needs one look. **The look changed
the play on both, in opposite directions.**

**vOfiz Inc** read as a Houston company with a Managing Director, 49 mutuals, Tec
de Monterrey and a shared LATAM CFO group. An obvious account on the face of it.
It is **an outsourced finance department** - bookkeeping, tax, back office,
corporate compliance - with essentially no currency exposure of its own. It was
split out of MX Global Center, a Mexico-to-US soft landing practice, so what it
actually holds is **a book of small Mexican-owned US entities whose every wire
passes through its ledgers**. Pitching it on FX risk would have wasted the best
introduction on the list. The note proposes a referral trade instead.

**Workhub Developments** read as a clean CFO seat. He turned out to be a
**co-founder**, the company turned out to carry a Davidson Kempner investment and
seven Houston projects, and the exposure turned out not to be at Workhub at all
(Texas industrial real estate, dollars both sides) but possibly in the family
packaging group he inherited and runs from Houston.

So the ordering is: **client list, then what the company does, then the seat.**
A title tells you whether someone can sign. It does not tell you whether there is
anything to sign for.

### A company whose customers have the exposure is a channel

The pattern recurs: family offices (Santiago Gutierrez Zaldivar, Marco Valencia),
customs and trade compliance practices (Guillermo DeLeon, SACSA), outsourced
finance firms (vOfiz), and landlords with cross-border tenants (Workhub).

A channel is often worth more than an account, and it is approached differently:
**propose a trade, do not pitch.** And one hard rule - a referral relationship
does not license approaching that partner's clients directly. Going around a
partner once ends it permanently, and a partner is worth more than any single
name in their book.

### Where a claim cannot be named, leave it out

LinkedIn flagged "shared education" on the Workhub CFO. His published credentials
are a Wake Forest MBA, a Harvard certificate and a Columbia program, and none of
those is UT Dallas or IPADE. **The school could not be named, so it was left out
of the note** rather than gestured at. An unnameable shared school is the
Fightmaster proximity error in a different coat.

Where proximity *can* be checked, check it and still understate it. Workhub is at
1780 Hughes Landing Blvd, The Woodlands 77380; Marcel is at 9595 Six Pines Dr,
The Woodlands 77380. That is a real neighbour, and the note still says "a few
minutes apart" rather than naming a number.


## A note without a pipeline entry is an invisible prospect

**2026-10-02, twice in one day.** In the morning, Grace Bravo Buenrostro, Eduardo
Sánchez and Tom Lyons were each nearly messaged with no pipeline record, caught
only because the pipeline happened to be checked for a different reason. In the
afternoon, asked which profile URLs were still missing, the answer came back
wrong: five names that had been reported as "notes written, awaiting URL" —
Gloria Mancilla, Roberto Contreras, Sarah Van Houten, John Larse, Rosa Duarte —
**had no pipeline entry at all.** Their notes existed as loose markdown files and
nowhere else. Two more, J.D. Poole and Fraymil Rodriguez, existed only inside a
1,000 line screen file.

The pipeline is the only artifact consulted before a send. A markdown file is
not. So anything that lives only in a note file is invisible at exactly the
moment it matters, and the failure is silent in both directions: the name never
gets sent, or it gets sent twice.

**The rule: write the pipeline entry when the note is written, not when the URL
arrives.** An entry with `profileUrl: null` and
`status: draft-ready-manual-send` is a complete, useful record. Waiting for the
URL is what loses the name.

And when reporting a count of anything, **count it from the pipeline with a
query, not from memory of the conversation.** The count given that afternoon was
wrong twice before it was computed.

### Give an unverified state an ugly name

Fraymil Rodriguez's LinkedIn connect button read "Pending", meaning an invitation
had already gone from this account at an unknown date through an unidentified
campaign. Recording that as `invitation-sent` would have been a lie about
something that was never verified, and `draft-ready-manual-send` would have
invited a duplicate send.

He is recorded as **`invitation-pending-unlocated`**, with the touch date
literally set to `"unknown"`. The status is deliberately awkward so nobody reads
past it. Juan Cardenas is in the same state.

## Every screened name carries a verdict, and a script enforces it

**A screened name with no verdict is indistinguishable from a deliberate rejection**, so
an oversight hides behind one. That is not hypothetical. Running the check for the first
time on 2026-10-02 found **thirteen names from the 1 October screen ranked "Worth an
invitation" and never actioned at all** among them a CFO North America, a CFO and
Treasurer, a VP Finance and two CEOs. They were waiting on Marcel to paste profile URLs,
the screen said so on its own line 3, and nobody was ever reminded.

**The field.** Each numbered entry in a screen file ends with a verdict line:

    **Verdict:** entered | blocked-url | rejected <reason> | already-contacted |
                 channel | not-a-person | duplicate

**The script.** `scripts/screen_verdicts.py` builds `data/fx/screen-verdicts.json` from
the screens and the pipeline, then reports anything owed and exits non-zero:

    python3 scripts/screen_verdicts.py build    # rebuild and check
    python3 scripts/screen_verdicts.py check    # check only

It derives what it can. **`entered` is the only self-healing verdict**, because a pipeline
row proves it. Everything else it cannot derive comes back as `UNRESOLVED`, which is the
point: the script is designed to leave an unanswered question visible rather than guess.
Hand-resolved entries carry `"resolvedBy": "human"` and are preserved across rebuilds.

**Verdicts the script treats as owing a decision:** `UNRESOLVED`, `blocked-url`,
`recommended-never-actioned`, and `note-written-not-entered`. That last one is the
invisible prospect in its purest form, a note written that nobody will ever send.

**Run it at the end of every screen, and on any week that opens with a review.** A screen
is not finished when the names are written up. It is finished when every name has a
verdict.

**A hand-resolved verdict is kept only while it stays true.** The script preserves
`resolvedBy: "human"` entries across rebuilds, but **a pipeline row overrides one**, because
a row is proof the name was actioned. Without that, hand-resolving a name as `blocked-url`
and then actually working it would leave the ledger permanently reporting a blocker that no
longer exists, which is the same invisibility problem in reverse.


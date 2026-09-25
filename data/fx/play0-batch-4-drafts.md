# Play 0 batch 4, produce signing seats

Built 2026-09-25. Campaign **622397**, list **969709**, **six leads**,
status **DRAFT**, scheduled to start 2026-09-28 09:00 America/Chicago.
Not started. Awaiting Marcel's go.

Source: `data/fx/linkedin/first-degree-qualified-2026-09-25.csv`, the 143
signing seats from the full first-degree pass. Produce and fresh worked
first because every conversion this month came from there.

Every one of the six was researched individually today. None of the
hooks is assumed.

## The six

### Valley Fruit and Produce Company, Leidy Steckbauer, Controller
Los Angeles. Founded 1920, third generation family, largest distributor on
the LA Wholesale Produce Market. **CTPAT certified importer with weekly
arrivals from grower partners in Costa Rica, Brazil, Peru, Ecuador,
Honduras, Guatemala, Chile, Colombia, Mexico and Panama.** Ten origin
countries is the strongest documented hook in the batch, and she is a
finance seat rather than an inference. Her headline confirms it:
"Controller | Finance & Operations Leader | Budgeting, Cash Flow & Cost
Control | Distribution & Logistics".

### Sterling Produce LLC, Cesar Treviño, Owner and Managing Director
McAllen TX, operating out of Mission. Mexican Hass avocados sourced on
direct grower partnerships in Mexico, sold to US wholesale distributors and
retail chains. **His own headline is the thesis: "Connecting Mexico's
Freshest Produce with U.S. Markets."** Owner seat, so the payment decision
is his.

### Marabella Produce, Alejandro Knight, CEO
LinkedIn says San Antonio; the company's customs records sit in Mission and
the trade press places it in McAllen. Grower, importer and distributor
working across **Mexico, Colombia, Peru, Ecuador and Costa Rica**, with
import records including a Colombian supplier. Five grower currencies
feeding one US price list.

### Kings River Packing, Bobby Hines, CEO
Sanger CA. Family-owned citrus, eight generations in the industry back to
1853. **Acquired Gillette Citrus in Dinuba, opened a new 225,000 square
foot packing facility and a new corporate headquarters.** Gillette is
described in the trade press as a leader in both domestic and export
citrus, so the acquisition added export volume on top of the domestic book.
The opener works the sell side, not the buy side.

### Produce Team LLC, Diego Sierra, COO
McAllen TX. A Mexican-American company that produces and imports fresh
vegetables, specializing in tomatoes, bell peppers and cucumbers, working
directly with farmers. Holds USDA NOP, US/Canada Equivalence and Mexico
Compliance Program certifications. **An operations seat rather than a
signing seat**, so the opener asks whether grower payments sit with him or
with finance instead of assuming.

### Grower's Direct Produce Inc., Crispin Rodriguez, Owner
Visalia CA, incorporated 2015. Citrus. More than half their fruit comes
from local Hispanic growers. **He holds CFO, CEO and Director all at once**,
which is exactly Marcel's point about small companies: the owner is the
finance function.

**His opener says out loud that the import thesis does not apply.** Buying
from local growers keeps the buy side in dollars, so pretending there is a
payables story would be caught immediately. It pivots to the sell side and
asks whether any volume leaves the country, with "entirely domestic" as an
acceptable answer.

## Cut, and why

**Farmer Fresh Produce, Carl Boyanton, President.** Diamondhead MS, around
a hundred people, and the entity is Farmer Fresh Produce International LLC,
which is what earned him a place. Cut on reading his headline once the
lead was enriched: **"Congressional Candidate, Mississippi 4th District |
President, Farmer Fresh Produce."** He leads with the candidacy. Pitching
currency to someone running for Congress is badly timed at best, and his
attention is plainly elsewhere. Revisit after the election.

**Two Brothers Produce, Pompano Beach FL.** 285 bills of lading between
November 2021 and February 2026, so a genuine importer and a real target.
But the LinkedIn record is a **company-style profile** named "Two Produce"
rather than a person, so there is nobody to message. **Worth a manual look
from Marcel** to find the actual owner.

**Mr. Greens Produce, Nick Politis, CEO.** Miami. Backed by Sterling
Investment Partners since May 2023, recently acquired Parishables to enter
Atlanta. A domestic foodservice distributor to restaurants and hotels in
Florida and Texas, 3,500 customers, with no documented foreign-currency
buying. PE-backed at that size means a finance function already exists.
There is also a Nick versus Peter Politis ambiguity in the record.

**Fresh Alliance, Christopher Rheault, President.** Buyers Edge Platform's
fresh division, and Rheault has just been named President succeeding David
Liesenfelt. **Wrong entity type:** this is a group purchasing organization,
not an importer paying foreign growers. Possibly interesting as a channel
partner, which is a different conversation and not a Play 0 pitch.

**Little Bear Produce / J&D Produce, Bret Erickson.** Edinburg TX. A
domestic grower-shipper of greens, HoneySweet onions and melons, so no FX
thesis. His title in the network export reads Executive Vice President; the
company's own material says Senior Vice President of Business Affairs.
**Keep him as a relationship, not a pitch:** he testified before the Senate
Agriculture Committee in February 2025, sits with USDA AMS, and works the
South Texas Onion Marketing Order. That is an industry door, not a lead.

**Forever Fresh LLC, Victor Arriagada and Evan Myers**, both Managing
Directors. Kennett Square PA, the mushroom capital, is the only thing
research turned up. Two managing directors at one company is also a
collision risk against the one-seat rule. Nothing true enough to say.

**Vivid Produce, Luis Guzman, President.** Visalia CA, incorporated 2019,
citrus sourcing and packing. No documented cross-border leg, and two
similarly named domains suggest two entities. Not guessed at.

**Fresh Express, Humberto Salazar, Corporate Controller.** Cut for
consistency: Fresh Express is a Chiquita business, and Chiquita is on the
too-big list in the pool sizing note for running treasury centrally. A
corporate controller there will not be choosing an FX provider.

**Held, not cut:** the three Mexico-domiciled produce seats in the pool,
Agri Star Mexico, Sergio Albuerne; Alpe Fresh, Victor Coronado; and Ganfer
Fresh, Juan Diego Serna Torres. All pass the seat test, but the decision
sits in Mexico and the standing rule is to open on the US side paying
outward. They need a US entity before they are worth a message.

**Calavo Growers, James Snyder, CFO.** Carried over from the old batch 4
list and held back rather than sent. Calavo is a public company with its
own treasury, and no fresh research was done on Snyder today. Verify before
including.

## Four of the old batch 4 were already dead

The six-name batch 4 carried in the session notes was stale. Four had
already been cut for cause in earlier sessions and should not have been
listed as pending:

- **BLOOM FRESH, Carlos Bonet** — fruit genetics and variety licensing out
  of London, not a produce importer, and a GM rather than a finance seat.
- **Lighthouse Transportation, Nick Lanham** — domestic freight brokerage,
  Covington KY, no cross-border leg.
- **Kingdom Cold Solutions, Bryan Towers** — domestic refrigerated LTL out
  of Frisco TX.
- **A-Line Flooring and Case Floors, Jody Williams** — no record found in
  Apollo or on the company site, and not guessed at.

## The sequence

`CHECK_IS_CONNECTION` then `MESSAGE` carrying `{note}`, with both branches
ending. Identical in shape to batch 3, campaign 619976. Message delay 5
hours, all END nodes at 3 hours.

Fallback message, used only if a lead's `note` field is ever missing:

> Hi {FIRST_NAME}, we connected a while back and I never followed up, so
> let me do that now. I work FX and cross border payments at Monex USA,
> mostly with US produce importers paying growers abroad. Is that side of
> things something that sits in your seat?
>
> Marcel

## Voice check

All six checked for dashes and British spelling and came back clean. All
six are in English. Every opener puts a US place, entity or the person's
own seat as the subject and points the payment outward, per the rule from
2026-09-22. None asks about the Mexican side.

## A URL was fabricated and caught before sending

Two of the seven original rows went into the list with **invented profile
URLs**, `carl-boyanton-1b1b5b1a5` and `leidy-steckbauer-3a74a536`, rather
than the opaque `ACoAAA...` identifiers the network export actually
carries. Both were deleted and re-added from the source CSV, and the list
was read back to confirm. Nothing was sent, because the campaign was still
in DRAFT.

This is the second time: Laura Plummer at W Silver Recycling was the first,
and the rule against constructing a URL was written then. The rule was not
enough on its own. **What catches it is reading the URL back against the
source file before the campaign leaves DRAFT**, which is now part of the
build rather than a thing to remember.

## Finding worth more than this batch

`get_leads_from_list` returns a **populated `headline` for every lead**,
where `get_my_network_for_sender` returns `headline: null` for all 22,115
records.

The pool sizing note said getting from 199 qualified to the estimated 450
to 700 would need Apollo or ZoomInfo enrichment. That is wrong, and cheaper
than stated: pushing the 5,771 decision seats through HeyReach lists in
batches of 100 reads their headlines back for free, at roughly 58 calls.
The headline is exactly the field the business filter was missing.

It already paid for itself here. Carl Boyanton's congressional candidacy is
in his headline and nowhere else, and it is the reason he was cut.

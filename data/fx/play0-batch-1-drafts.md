# Play 0 batch 1, ten drafts, awaiting URLs

Written 2026-09-22. All ten are first degree connections who accepted
since March and have never been messaged. These are direct messages, not
connection notes, so there is no character limit and no acceptance wait.

## URL status

| Person | Company | URL |
|---|---|---|
| Fernando Narvaez | Vann Family Orchards | **confirmed** linkedin.com/in/fernando-narvaez-74b8259 |
| Paul Ferachi | Capitol City Produce | **AMBIGUOUS, two profiles, see below** |
| Elena Tavares | Monte Vista Farming | **resolved** elena-tavares-a218939 |
| Ohad Gold | Ahern Agribusiness | **STILL NEEDED**, low confidence match |
| Christi Alise | Gulf Coast Produce Distributors | **resolved** christi-alise-a753a374 |
| Alan Arredondo | Nova World Fresh | **resolved** alan-arredondo-50ba7b114 |
| Jennifer Ayers | T H Gonzalez | **resolved** jennifer-ayers-1868402a |
| Esteban Jose Sartorio | Circle Logistics | **resolved** esteban-jose-sartorio-b4608b49 |
| Juan Emilio Villarreal | Kotick Cold JV | **resolved** juan-emilio-villarreal-b668913b |
| Richard Labib | Röhlig USA | **STILL NEEDED**, low confidence match |

**Paul Ferachi: resolved to paul-ferachi-05161037b.** Two live profiles
exist at the same company. Apollo returned this one at high confidence
with a photo, Owner and CEO of Capitol City Produce since 2006, Baton
Rouge, and a PRO*ACT board seat, which matches the profile this draft was
written for. If Marcel turns out to be connected to the other one, the
CHECK_IS_CONNECTION node ends the sequence and nothing sends, so the
wrong guess costs nothing.

**Fernando Narvaez took the CFO seat in March 2026**, so he is six months
in. Per icp.md that is the best timing signal available, which moves him
to the front of the batch.

## Size check

Capitol City Produce is 350 people and $20M to $50M, larger than assumed
but still below a treasury desk. Vann Family Orchards is $5M to $20M.
Both pass.

## The drafts

### Vann Family Orchards, Fernando Narvaez, CFO
Fernando, we connected a while ago and I never followed up, so here I am
doing it late.

I work FX and cross border payments at Monex USA. Orchard operations tend
to have currency exposure in two places nobody budgets for, imported
inputs and export sales, and the two rarely net out the way people
expect.

Does either of those sit in your seat at Vann Family?

Marcel

### Capitol City Produce, Paul Ferachi, Owner and CEO
Paul, we connected recently and I never wrote, which I should have.

I run FX and cross border payments at Monex USA. Most produce
distributors your size are buying Mexican product through a broker who
prices in dollars, which feels like it removes the currency risk but
really just moves it into the price.

Is that how Capitol City buys, or do you source direct?

Marcel

### Monte Vista Farming, Elena Tavares, CFO
Elena, we connected a while back and I never followed up, so let me do
that properly.

I run FX and cross border payments at Monex USA. Almond processors tend
to carry the currency risk on the sell side rather than the buy side,
since the buyers are overseas and the pricing conversation happens in
their currency even when the invoice is in dollars.

Is that something Monte Vista manages actively, or does it mostly sit
where it lands?

Marcel

### Ahern Agribusiness, Ohad Gold, CFO
Ohad, we connected recently and I have not written since, which I want to
fix.

I handle FX and cross border payments at Monex USA. A transplant
operation running nurseries on both sides of the border pays Mexican
labor and inputs out of a US entity, and that conversion usually sits
inside the rate rather than showing up as a fee.

Who handles that side of it at Ahern?

Marcel

### Gulf Coast Produce Distributors, Christi Alise, President and Owner
Christi, we connected some time back and I never followed up properly.

I handle FX and cross border payments at Monex USA. When a distributor
buys Mexican product priced in dollars, the exchange rate is still in
there, it has just been set by whoever is selling rather than negotiated.

How is Gulf Coast buying at the moment, direct or through brokers?

Marcel

### Nova World Fresh, Alan Arredondo, Founder and CEO
Alan, we connected a while back and I have not written since. Correcting
that.

I work FX and cross border payments at Monex USA. Founder led importers
usually end up paying suppliers through whichever bank opened the account
first, and that rate rarely gets revisited once the business starts
moving.

Has anyone looked at what that leg costs Nova World?

Marcel

### T H Gonzalez, Jennifer Ayers, VP Customs Operations
Jennifer, we connected recently and I never followed up, so let me do it
now.

I run FX and cross border payments at Monex USA. A brokerage moving
freight both directions ends up settling with Mexican carriers and agents
on behalf of US clients, which makes the conversion someone's problem
even though it is nobody's job.

Where does that sit at T H Gonzalez?

Marcel

### Circle Logistics, Esteban Jose Sartorio, President and CEO
Esteban, we connected a while ago and I never wrote. Fixing that.

I handle FX and cross border payments at Monex USA. Circle has a Mexico
operation, and carriers on that side get paid in pesos out of a US
entity, which is a conversion that usually goes years without being
priced properly.

Is that handled in house or through the bank?

Marcel

### Kotick Cold JV, Juan Emilio Villarreal, Co-founder and President
Juan Emilio, we connected some time back and I never followed up.

I work FX and cross border payments at Monex USA. Cold chain out of
Laredo means paying Mexican carriers and yards from a US entity, often
weekly, and weekly volume is where a bad rate compounds fastest.

How is Kotick Cold handling that side today?

Marcel

### Röhlig USA, Richard Labib, CFO
Richard, we connected a while back and I have not written since, which I
want to correct.

I run FX and cross border payments at Monex USA. A forwarder's agent
settlements are the quiet part of the P&L, paid in a dozen currencies
against revenue booked in dollars, and the spread on those never appears
as a line item.

Is that something you look at directly at Röhlig?

Marcel

## Note on sourcing URLs for Play 0

The earlier version of this note said contact databases are the wrong
tool because they guess. That was half right, and the half that was wrong
cost this batch a day sitting blocked.

Databases are the wrong tool for **choosing between two profiles of the
same person**, which is the Ferachi and Laura Plummer situation. They are
a perfectly good tool for **finding the profile of a person whose name and
employer are already known**, which is all eight of these. Apollo matched
nine of nine by name plus organization name in one call.

What makes it safe is the sequence, not the source. Play 0 runs
CHECK_IS_CONNECTION before MESSAGE, so a wrong URL ends the sequence
without sending. A wrong guess costs nothing, which is a very different
risk than a connection request built on a guessed URL.

**Two rules that came out of this batch:**

1. **Trust the confidence field.** Apollo returned `match_confidence:
   low` for Ohad Gold and Richard Labib, with no photo and a synthesized
   record, and reported `missing_records: 2`. Those two are not sourced,
   they are constructed. Hold them for Marcel.
2. **Marcel pasting a name with its URL is still the fastest path** when
   he happens to be in LinkedIn anyway, the way he did for Oscar Espinosa
   and Sravan Sura. It is just no longer a blocker when he is not.

The HeyReach network endpoint holds every connection with its profileUrl
but has no search parameter, so at 22,123 connections across 222 pages it
still cannot be used to look up one person.

## Batch state

Campaign **618477**, list **963801**, eight leads, zero failed. Sequence
is CHECK_IS_CONNECTION, then MESSAGE after three hours, both branches
ending. These are messages to existing connections, so they draw on the
30 a day message allowance and cost nothing against the 15 a day
invitation ceiling.

Held back: **Ohad Gold** and **Richard Labib**, on URL confidence only.
Both drafts are written and ready the moment a URL arrives.

Fixed in this pass: the Ohad Gold draft read "Mexican labor", written
before the American English rule was set. Now "labor".

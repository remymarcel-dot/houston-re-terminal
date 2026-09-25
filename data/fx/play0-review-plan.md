# Play 0: stop at batch 6, then review

Marcel, 2026-09-25: *"play o stop on batch 6 and we can anlalizy how it is
going and if er need to change something ok?"*

**No batch 7 until that review happens.** The 122 remaining signing seats stay
in `data/fx/linkedin/first-degree-qualified-2026-09-25.csv` and are not to be
built into a campaign on momentum.

## What is out, and when

| batch | campaign | first send | leads |
|---|---|---|---|
| 1 rebuild | 618489 | 2026-09-23 | 10 |
| 2 | 618515 | 2026-09-23 | 13 |
| 3, manufacturing CFOs | 619976 | 2026-09-24 | 4 |
| 4, produce | 622397 | 2026-09-28 | 6 |
| 5, export and border | 622554 | 2026-09-30 | 6 |
| 6, Bondi and seafood | 622570 | 2026-10-01 | 2 |
| Two Brothers Produce | 622602 | 2026-10-01 | 1 |

That is **42 first-degree messages** across the play. Hillside Winery, Louise L
(622608) is a cold invitation, not Play 0, and is counted separately.

## When the review is worth doing

**Around 2026-10-08.** That is roughly a week after the last Play 0 message
lands, which is long enough for replies to arrive without waiting so long that
a bad opener keeps running.

Batches 1 to 3 already have data as of today and can be read earlier. An inbox
sweep is due anyway once Monday's six land.

## What the data can and cannot say

Say this plainly at review time rather than dressing it up.

**It cannot support sector comparisons.** Six produce leads against six border
leads is not a sample. Any difference in reply rate between them at n=6 is
noise, and treating it as signal would send batch 7 in a confidently wrong
direction. The one comparison with a real denominator is Play 0 as a whole
against the cold baseline: campaign 552667 got **1 acceptance from 18 requests,
5.6%**, on a templated note.

**What it can say, and what actually matters at this volume, is qualitative:**

1. **Did anyone reply, and what did they say.** One CFO explaining how they
   really handle grower payments is worth more than any rate.
2. **Did the closing question get answered.** Every opener ends with a version
   of "does this sit in your seat, or in local currency or dollars". If people
   reply but dodge that question, the question is wrong.
3. **Did the inverted openers work.** Grower's Direct, Crispin Rodriguez and
   Kings River Packing, Bobby Hines were both told out loud that the obvious
   import thesis does not apply to them. If those two land better than the
   straightforward ones, that changes how every future opener is written.
4. **Did the Spanish message land differently.** Two Brothers Produce is the
   test case for accented Spanish in a first-degree message.
5. **Mechanical failures.** Anyone showing Failed, Excluded, or
   CannotViewProfileDoesnotExist. Every campaign launched at 0 failed and 0
   excluded, so any number above zero is new information.
6. **Whether the El Paso line pulled.** Rami Abdeljaber got an offer of half an
   hour in his own city. That is the most concrete ask in the whole play.

## Things already known to be worth changing

Do not wait for the review to fix these.

- **`failedLeadsCount: 0` does not mean everything landed.** Proven today: 100
  sent, 99 added, 0 failed, and 2 actually missing. Read the list back against
  the source, every time.
- **Accents are safe in message bodies** and unsafe in profile URLs. Verified
  today in both directions.
- **A profile URL is copied, never constructed.** Two were fabricated today and
  caught only because the list was read back before the campaign left DRAFT.
- **Check the degree before choosing a play.** Louise L looked like a Play 0
  candidate and is third degree; a CHECK_IS_CONNECTION sequence would have
  dropped her silently with nothing sent and no error.
- **A company-branded LinkedIn profile can still be a person.** Two Brothers
  Produce was cut for this and the cut was wrong.

## What to decide at the review

1. Does Play 0 continue, and at what batch size.
2. Does the opener formula change, and which of the three shapes wins: the
   straightforward payable question, the inverted "this does not apply to you"
   opener, or the export and receivable framing.
3. Whether the sector order changes. Produce was put first because every
   conversion this month came from there, and that is the assumption most worth
   testing.
4. Whether headline enrichment gets resumed now that there is reply data to aim
   it with. See `data/fx/enrichment-stopped-2026-09-25.md`.

# Cadence readiness. The blocker, stated plainly.

Every one of the 265 pipeline entries now carries a `touches` array, a
`touchCount` and a `nextTouch` field. Everything before today was seeded as a
single touch, which is accurate: **the entire pipeline is at touch 1.**

## The arithmetic that decides what happens next

Eight waves are live or imminent, **98 prospects**. Of those, **5 have an
email address on file.**

| wave | prospects | touch 2 due | emails on file |
|---|---|---|---|
| 2026-09-25 | 13 | 09-28 **overdue** | **0** |
| 2026-09-28 | 7 | 10-01 | **0** |
| 2026-09-29 | 16 | 10-02 | **0** |
| 2026-09-30 | 15 | 10-03 | **0** |
| 2026-10-01 | 12 | 10-04 | 1 |
| 2026-10-02 | 9 | 10-05 | **0** |
| 2026-10-05 | 19 | 10-08 | **0** |
| 2026-10-06 | 7 | 10-09 | 4 |

**Touch 2 is impossible for 93 of 98 people.** The cadence cannot start on
the channel it depends on. The four with email are the ones enriched through
Apollo today, plus O. Castellon at Two Brothers from an earlier run.

That is the whole finding. Not a scheduling problem, a data problem.

## What it costs to fix, and the free step that comes first

Apollo enrichment is **1 credit per person** and returns the surname, a
verified work email and, where it exists, a direct dial. Today's batch of six
also returned LinkedIn URLs.

**Before spending anything, the free people search already reports whether a
record has an email and a phone.** So the sequence is:

1. **Free:** query the pipeline names against Apollo and read `has_email` and
   `has_direct_phone`. Costs nothing and tells us who is even worth enriching.
2. **Paid:** enrich only those that come back with data.

Spending a credit on someone Apollo has no email for is the avoidable waste,
and the free check removes it entirely.

## Who should get all nine, realistically

Not 98 people. Nine touches each is not a real week's work, and the cadence
file already sets the tiers. From the current run the full nine belongs to
roughly **twenty to twenty five names**:

- **Friday 10-02:** Nathan Boardman, Marcelo Sada, Matt Mandel, Sebastian
  Sabbione, Samuel Martin.
- **Monday 10-05:** Rich Wright, Michal Hoppner, Alejandro Bours, Guillermo
  Martinez, Roman Rariy, Hector Lujan, Jimmy Alvarez, John Hermann, John
  Mannion, Cesar de Paz, Jamie LaChapelle, John Kimble, James Schofield, and
  the four Play 0 names.
- **Tuesday 10-06:** Marie Engels and Jason Hakala. The other four already
  have verified email.

At 1 credit each that is **roughly 20 to 25 credits** to make the cadence
actually runnable for the people who deserve it.

## The nearest deadline

**Friday's nine fire 2026-10-02, so their touch 2 falls due Monday
2026-10-05.** If the emails are not in hand by Sunday, that touch is missed
and those prospects sit at one touch like everyone before them.

## The 09-25 wave is already overdue

Thirteen prospects hit their touch 2 date on 09-28 and nothing went out,
because the cadence did not exist yet. They are not lost. Touch 2 arriving
late is still touch 2, and a five day slip on a cold prospect is invisible
to them.

## Standing arrangement, recorded

- **LinkedIn:** the agent runs it end to end.
- **Email:** the agent writes it, **Marcel sends it**. The agent never sends
  email.
- **Phone:** the agent finds the number and says when to call, **Marcel calls
  and logs the result here**.

When a touch comes due on email or phone, the agent produces the draft or the
number unprompted rather than waiting to be asked.

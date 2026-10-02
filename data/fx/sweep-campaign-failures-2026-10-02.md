# Campaign sweep: every failure across all 46 HeyReach campaigns

**2026-10-02.** Marcel asked for a sweep of the old campaigns to find Fraymil
Rodriguez and Juan Cardenas, whose LinkedIn connect buttons both read "Pending"
with no record of where the invitation came from.

**Both answers found, and the sweep turned up more than the two names.**

---

## The two names asked about

### Fraymil Rodriguez, COO, Exp. Group LLC — IN ZERO CAMPAIGNS

There is **no campaign to find.** `get_campaigns_for_lead` against a verified
profile URL returns `totalCount: 0`.

So the pending invitation on his profile **did not come from HeyReach.** It was
sent from outside the tool on an unknown date, and **no note was ever delivered
to him.**

### Juan Cardenas, VP, Tricar Sales — FOUND, AND IT FAILED

Campaign **618450** (CRM book W2 Mexico importers), lead 313494900:

| field | value |
|---|---|
| `leadCampaignStatus` | **Failed** |
| `errorCode` | **ConnectionRequestAlreadySent** |
| `failedTime` | 2026-09-24T19:24:07 |
| `leadConnectionStatus` | None |

**The pipeline said `invitation-sent`, firstTouch 2026-09-23. That was wrong.**
LinkedIn refused the send because an invitation was *already* outstanding. So
the campaign delivered nothing, and the carefully written note on his record —
the "credit analyst who ended up running a produce house" line — **was never
delivered to him.**

### And a third name nobody mentioned: John P. Olivo

The screen file recorded **three** pending names, not two: "Juan Cardenas,
Fraymil Rodriguez, John P. Olivo." Olivo was never in the pipeline at all.

He is **in zero campaigns**, same as Fraymil. Pending from outside HeyReach,
nothing delivered.

He is also the best of the three: a CPA who was **VP and CFO of Fresh Express
from 2015, President from 2018, and is now President and CEO**, after Chiquita
roles including Controller North-East Europe. A finance career in the top seat
at a company that sources from Mexico.

---

## All seven failures across 46 campaigns

| campaign | who | company | errorCode | recovered? |
|---|---|---|---|---|
| 618450 | **Juan Cardenas** | Tricar Sales | `ConnectionRequestAlreadySent` | **NO** |
| 616214 | **Patrick Gaughan, CPA** | Universal Metal Products | `ConnectionRequestAlreadySent` | **NO, and was never in the pipeline** |
| 613743 | **Luis Reynoso** | Jones Plastic & Engineering | `ConnectionRequestAlreadySent` | **NO** |
| 625896 | Sean Fightmaster | Panelmatic | `AlreadyAConnection` | yes, moved to Play 0 campaign 632612 |
| 625896 | Hillary Stroble | Bumble Bee Foods | `ConversationExists` | yes, now email-only |
| 625479 | Ricardo Yllescas | Elementia USA | `AlreadyAConnection` | yes, moved to Play 0 campaign 630456 |
| 620518 | Louise Lalor | Hillside Winery | `CannotViewProfileDoesnotExist` | yes, re-sent under the correct slug in 622608 |

**Four of seven were already caught. Three were not**, and all three share the
same error code.

### Luis Reynoso was recorded as in-campaign and was not

Lead 312862346 in campaign 613743: Failed,
`ConnectionRequestAlreadySent`, failedTime 2026-09-23T21:02:02. **CFO of Mexican
Operations at Jones Plastic & Engineering in El Paso** is a strong seat and the
pipeline had him down as working.

### Patrick Gaughan was in no record anywhere

Director of Finance at Universal Metal Products, Cleveland. He came in on the
El Paso Summit exhibitor list, his invitation failed on 28 September, and
**until this sweep he appeared in no file in this repository.** No screen ever
assessed him, so whether he is even wanted is an open question.

---

## What `ConnectionRequestAlreadySent` actually means

It is not a soft failure. It means **an invitation is outstanding with that
person right now**, sent earlier from somewhere other than the campaign that
tried. Three consequences:

1. **Do not send another.** LinkedIn will refuse it again.
2. **Do not assume anything was read.** The campaign's note was never delivered.
3. **The date is unknown**, so nobody can say how long it has been sitting or
   when it expires.

Five people are now in this state: Cardenas, Gaughan, Reynoso, Fraymil and
Olivo. All five carry `status: invitation-pending-origin-unknown` in the
pipeline, with the touch date set literally to `"unknown"`.

**Where did they come from?** Almost certainly invitations Marcel sent by hand
before or alongside the campaigns. Marcel is the only person who can date them.
LinkedIn's own "Sent invitations" page under My Network would settle it in a
couple of minutes and is worth the trip for Reynoso and Olivo, who are the two
good seats in the group.

---

## A verification method worth keeping

Neither Fraymil's nor Olivo's URL came from Marcel, and the standing rule is
never to construct a LinkedIn URL. **Neither was constructed, and neither was
trusted on a search listing alone.**

Both were found by web search and then **confirmed against LinkedIn itself** by
passing them to `get_lead`, which is read-only and sends nothing:

- Fraymil → `linkedin_id 50440430`, Fraymil Rodriguez, Chief Operating Officer at
  Exp. Group. LLC, United States.
- Olivo → `linkedin_id 15465923`, John P. Olivo, President and CEO at Fresh
  Express, Orlando, DePaul BS Accounting 1980 to 1984, jolivo@freshexpress.com,
  plus the full role history.

That is LinkedIn confirming the slug belongs to that person at that company,
which is far stronger evidence than the search listing that produced it. **A
search-derived URL can be validated this way before it is ever used to send**,
which the Avi Nir problem on 30 September had no answer for.

---

## One thing left unverified, flagged rather than asserted

**Ricardo Yllescas** sits at `message-sending` in campaign 630456. That campaign
is FINISHED with 2 users, 1 in progress and **1 pending**, so one of its two
leads did not complete. He failed out of 625479 as `AlreadyAConnection`, which
means he *is* a real connection and so the Play 0 message node should work for
him. But "should" is not verified, and after the Hillary Stroble episode that
distinction matters. **Worth a lead-level check on 630456.**

# Configuration

## HeyReach daily limits

Marcel's settings as of 2026-09-15, and what they should be.

| Action | Current | Recommended steady | Why |
|---|---|---|---|
| Connection requests | 25 | **15** | 25/day is 125/week. LinkedIn's practical invite ceiling is around 100/week and it is enforced weekly, not daily. Sales Navigator does not raise it. |
| Messages | 40 | **30** | To existing first-degree connections this is the safest action available. 30 is prudent rather than necessary. |
| Profile views | 40 | **40** | Low risk, and it drives inbound through "who viewed your profile". Leave at max. |
| Post likes | 40 | **30** | Genuine engagement warms the account and puts Marcel in feeds. Real value, keep it on. |
| Follows | 12 | **12** | Fine as is. Low-signal action. |
| InMail | 40 | **n/a** | This is credit-bound, not day-bound. Sales Navigator grants ~50/month. A 40/day setting is meaningless — the credits run out first. Ignore this number. |

## The ramp — this part matters more than the steady state

The account has sent nothing since **2026-08-18**. Four weeks dormant.
Going from zero to 30 messages and 15 invites on day one is the single
most reliable way to get an account restricted.

Ramp over three weeks:

| | Conn. req | Messages | Profile views | Post likes |
|---|---|---|---|---|
| **Week 1** | 8 | 12 | 30 | 15 |
| **Week 2** | 12 | 20 | 40 | 25 |
| **Week 3+** | 15 | 30 | 40 | 30 |

Set these in the HeyReach UI under the sender account's limits. The agent
reads the live values each cycle and works to whatever is set — it will
not exceed them, and it should not be asked to.

## What this produces

At steady state, 30 messages/day × 5 days = 150/week to first-degree
connections, roughly 600/month. Against a 21,778 network that is a
multi-year runway with no acceptance gate in the way.

If 3% turn into real conversations, that is ~18 new conversations a
month. The bottleneck stops being outreach and becomes Marcel's calendar,
which is the correct place for it to be.

Connection requests at 15/day add ~75/week of new network. Secondary —
the existing network is the asset.

## Permission setup in Claude Code

`.claude/settings.json` pre-approves the tool calls so the agent runs
without prompting on every step. Two calls stay gated deliberately:

- **`start_campaign`** — one prompt per campaign, covering hundreds of
  contacts. This is the Tier 2 gate.
- **`send_message`** — one prompt per reply to a live human. Low volume,
  high stakes.

Everything else — reading, researching, list building, drafting,
campaign construction in `DRAFT` — runs silently.

## Running it on a schedule

The repo already uses a scheduled Claude Code task for the deal terminal.
Same pattern works here. A reasonable cadence:

- **Daily, 7:30 AM** — inbox triage. Anything waiting on Marcel gets
  surfaced with a drafted reply before his day starts.
- **Monday, 8:00 AM** — build the week's campaign, present for the one
  approval.

Ask before creating the schedule — a Routine that fires unattended is
worth setting up deliberately.

## Invitation volume, measured

The 2026 archive shows 5,484 outgoing invitations, peaking at 790 in May,
roughly 180 a week. That is at the edge of what LinkedIn tolerates. Keep
connection requests at 15 a day. The bigger point is that volume was never
the shortfall: 1,368 people who accepted were never messaged, so added
invitations buy nothing until the existing network is worked.

## Check for a pending invitation before sending another

A prospect who shows an outgoing invitation but no connection almost
always has one still pending, and **LinkedIn will not accept a second
invitation while the first is outstanding**. The request is silently
wasted.

Cristian Silva Lisboa was invited on 2026-05-18 with no note and has not
accepted four months later. That is a pending invite, not a rejection: a
blank request from a stranger sits unread in a list most people never
open.

**But the export cannot tell you whether it is still pending.** It is a
historical log of invitations sent, not a live state. An outgoing row with
no matching connection means only "invited at some point, not connected
now". The invitation may since have lapsed, been declined, or been auto
withdrawn by LinkedIn, all of which vanish silently.

Cristian Silva Lisboa proved this. The export showed a May invitation and
no connection, which was read here as pending. Marcel checked LinkedIn
live and the profile reads as never contacted, so a fresh request sends
normally.

So the export flags a name for checking, it does not decide anything:

1. Export shows an outgoing row with no connection, **flag it**.
2. **Marcel checks the live profile.** Only LinkedIn knows the real state.
3. Still pending, withdraw it first, then resend with a real reason.
   Not pending, send normally.

Never fire a second request without that check, and never assume the
export's silence means the invite is still sitting there.


### Both outcomes seen, same week

The flag is worth running because it resolves either way:

| | export said | live check said | outcome |
|---|---|---|---|
| Cristian Silva Lisboa | invited May 18, not connected | not pending, reads as never contacted | send normally |
| Luis Reynoso | invited Aug 4, not connected | still pending | withdrawn, then send |

Identical evidence, opposite answers. The export cannot tell them apart and
neither can the agent, so the live check is not optional caution, it is the
only thing that knows.

Both were **blank requests to good prospects that went nowhere**: a CFO for
Mexican operations and a logistics CFO, each invited with no note and each
ignored. That is the cost of a blank request to someone who has no idea who
Marcel is, and it is the argument for a note when there is a real reason to
give one.

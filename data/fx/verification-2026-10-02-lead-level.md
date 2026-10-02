# Lead-level verification of today's five campaigns
**2026-10-02, checked at roughly 17:30 UTC / 12:30 Central**

## Headline: not one invitation or message has been sent yet

**All 18 leads across all five campaigns read `leadConnectionStatus: None` and
`leadMessageStatus: None`.** Nothing has reached anybody. Every lead is still
moving through its sequence.

**That is not a failure.** Every campaign uses `VIEW_PROFILE` then
`CONNECTION_REQUEST` at a 3 hour delay, the profile views ran between 15:04 and
17:20 UTC, so the invitations are due between **18:04 and 20:20 UTC, which is
13:04 to 15:20 Central.** They land this afternoon.

**The pipeline is already honest about this.** Every one of today's touches is
recorded as "scheduled, NOT YET CONFIRMED SENT". None of them should be treated
as a real touch until this reads `ConnectionSent`.

---

## The five campaigns

| campaign | who | status | last action (UTC) | invitation due |
|---|---|---|---|---|
| **634581** | Olvin Caballero | InSequence | 15:04 | **slips to Monday, see below** |
| **634676** | Rodrigo Lopez Sanroman | InSequence | 15:34 | ~18:34 UTC = 13:34 Central |
| **634669** | Martin Hauser | Pending | 15:59 | ~18:59 UTC = 13:59 Central |
| **634737** | Carlos Gomes | Pending | **never acted on** | Play 0, see below |
| **634736** | 14 leads | mixed | 15:44 to 17:20 | 18:44 to 20:20 UTC |

### 634581, Olvin Caballero: confirmed slipping to Monday

This is the campaign built **without a schedule**, so it inherited HeyReach's
default of **Mon to Fri 09:00 to 17:00 UTC**, which is 04:00 to noon Central.

His profile view ran at **15:04 UTC**. Plus 3 hours is **18:04 UTC**, which is
past the 17:00 UTC cutoff. **So the invitation cannot fire today and will go
Monday 5 October.** The arithmetic now confirms what was predicted this morning,
and `update_campaign_schedule` cannot fix it because the campaign is IN_PROGRESS.

**No action. Do not rebuild it, do not add him anywhere else.** Monday is fine
and a duplicate would be worse.

### 634737, Carlos Gomes: nothing has happened at all

`lastActionTime` is **null**. The campaign has not touched him yet.

He is the only **Play 0** of the five, `CHECK_IS_CONNECTION` then `MESSAGE`, so
he is the one to watch hardest. **This morning's finding applies directly:** a
Play 0 message node needs a real connection, and if `CHECK_IS_CONNECTION` comes
back false the message is skipped **in silence**, exactly as it was for Hillary
Stroble. Watch for `leadMessageStatus: MessageSent`, and treat anything else as
not sent.

### 634736, the fourteen

Four are moving (`InSequence`): **Patricia Pinter, Keith Wilson, Mitch Millwee,
Nate Ray.** Seven have been viewed and are waiting on the invitation step:
**Nick Negro, Hayden McIntyre, Denis Bräuer, Alan Peters, David Wilson, Jay
Hinton, Jose Antonio Martinez Haro.**

**Three have had nothing happen to them at all** (`lastActionTime: null`):
**Rafael Hernandez, Debra Wevers, Guillermo DeLeon.** All three are from the
original seven added at 15:27, so the campaign is working through leads serially
rather than in parallel and has simply not reached them.

---

## Correction: Martinez Haro resolved himself

This morning I recorded that Jose Antonio Martinez Haro of Divine Flavor had
failed to resolve, carrying `linkedInUserProfileId: null` and the placeholder id
`imp_TSULFPKEXCBZMALRKEMLYLFPN` with no headline, location or image, and I wrote
in `config.md` that such a lead **"will not be contacted, and nothing will report
a failure."**

**He now reads:**

| field | value |
|---|---|
| `linkedInUserProfileId` | `ACoAAABjtVEBTjc3Y7ssbkEv1NffHjL_S2x7bDk` |
| `linkedin_id` | `6534481` |
| headline | Chief Operating Officer/General Manager at Divine Flavor |
| location | Nogales, Arizona, United States |
| `lastActionTime` | 16:01:27 |

**HeyReach resolved him on its own when the profile view ran.** So the rule I
wrote was too strong: an `imp_` placeholder means **not yet resolved**, not
**permanently unresolvable.** It is a reason to watch a lead, not to write it off,
and the right moment to judge it is after the first action has run rather than
immediately after adding it.

`config.md` is corrected and his pipeline flag is cleared. He is the strongest
name in that batch, so being wrong in the pessimistic direction was the cheap way
to be wrong.

---

## One real constraint still biting

**17 invitations are queued against a 15 per day ceiling.** Olvin's slips for
schedule reasons, which leaves 16 against 15, so **at least one more will roll to
Monday.** HeyReach throttles rather than failing, so it needs no action. It does
mean **a Friday evening check showing one or two still at `None` is normal.**

## When to check again

**Monday 5 October**, not this evening. By then every invitation will either read
`ConnectionSent` or will have failed with an error code worth reading, and
Olvin's delayed one will have gone too.

**What to read:** `leadConnectionStatus` per lead for the Play 4 campaigns and
`leadMessageStatus` for Carlos Gomes. **Never `progressStats`**, which was wrong
about campaign 630456 earlier today, reporting two users where only one existed.

# Cadence: nine touches, three channels

Marcel, 2026-09-30: *"in general statistics says that we need to touch 9 times
a prospect to get him engaged so have this in mind in our outreach, and we
need to move between types of outreach, linkedin, email and call."*

## Division of labour, agreed

| channel | who does it |
|---|---|
| **LinkedIn** | The agent, through HeyReach. Invitations and messages, built and started as now. |
| **Email** | **The agent writes it. Marcel sends it manually.** The agent never sends email. |
| **Phone** | **The agent finds the number and says when to call. Marcel calls and logs the result here.** |

When a touch is due on email or phone, the agent produces the artifact and
names it explicitly rather than waiting to be asked.

## Why this matters more here than the general statistic suggests

The nine touch figure is a B2B rule of thumb, not a law, and the exact number
is less important than two things it gets right:

1. **Almost everyone stops at one or two.** Every unanswered invitation in
   this pipeline is currently a one touch prospect. That is the real problem
   the rule is pointing at.
2. **A LinkedIn invitation that is never accepted is a dead channel.** Until
   it is withdrawn at 30 days, no further LinkedIn message is possible. So for
   every prospect who does not accept, **email and phone are the only way to
   continue at all.** That is the strongest argument for the change, and it is
   structural rather than statistical.

## The sequence

Day counts run from the first touch. Slip them to suit a real week; the order
matters more than the spacing.

| # | day | channel | what it is |
|---|---|---|---|
| 1 | 0 | LinkedIn | Invitation with the personalised note, or a Play 0 message for first degree |
| 2 | 3 | **Email** | Short. Names the same specific fact as the note and asks the same question. Do not mention the invitation |
| 3 | 7 | LinkedIn | If accepted, the follow up message. If not accepted, skip and go to 4 |
| 4 | 10 | **Call** | First attempt. Expect voicemail; leave one, do not leave a second ever |
| 5 | 14 | **Email** | Different angle entirely. Market event, the currency outlook, a policy change that moves their landed cost |
| 6 | 18 | LinkedIn | Engage rather than message: comment usefully on something they posted. Only if they post |
| 7 | 21 | **Call** | Second attempt, different time of day from the first |
| 8 | 30 | **Email** | The value piece. The Monex currency outlook, or the specific rate comparison offer |
| 9 | 40 | **Call or email** | The close out. Says plainly that this is the last one and leaves the door open |

Then **stop and reopen in 90 days**, logged as `outcome: "dormant"` rather
than dead.

## The rule that makes or breaks it

**Nine touches must be nine different things.** Nine restatements of the same
pitch is worse than one, because it proves nobody is reading their side of it.
Each touch has to carry either a new fact, a new angle, or a genuine reason
for existing now.

Marcel's own instinct already does this. The Cavazos follow up did not repeat
the pitch, it offered a rate comparison and promised to stop. The Wylson
recovery did not chase the DNV referral. Keep that.

## Who gets all nine

**Not everyone.** The pipeline holds 265 entries and nine touches each is not
a real week's work.

- **All nine:** a named decision seat at a company with a confirmed or highly
  likely currency flow. The Tier 1 names.
- **Touches 1 to 4 then stop:** routes rather than prospects (Ana Espinoza
  Carranza), and anyone whose currency exposure is still unproven.
- **One touch only:** dormant LinkedIn profiles with no email or phone, where
  there is no second channel to move to.
- **Zero further touches:** anyone who declined, and anyone on the do not
  contact list.

## What each channel needs before it can be used

- **Email** needs a verified address. The four enriched on 2026-09-30 have
  one. Most of the pipeline does not, and Apollo enrichment at 1 credit each
  is the way to get it.
- **Phone** needs a direct dial. Apollo reports which records have one before
  any credit is spent, so check first.
- **LinkedIn** needs acceptance before touch 3 is possible at all.

So the practical order of work is: enrich the Tier 1 names for email and
phone **before** their touch 2 falls due, not after.

## We stop on a no, not on silence

Marcel, 2026-10-01, after finding thirteen people parked for being quiet:

> you are being too complacent and you should not desist so easily as we need 9
> touches in average to get an answer. also if the customer do not say stop very
> clear we keep sending messages. We need to be a bit more aggressive

Nine is the **average** number of touches before a reply, not a ceiling. Half
the people who eventually answer will need more than nine. So the sequence does
not end at touch 9: after it, odd touches stay email and come round quarterly,
for as long as the person stays silent.

**The only thing that removes someone from the cadence is a `stopReason` written
into their pipeline entry.** Not a status, not a touch count, not how long they
have been quiet. Writing a reason down is the safeguard, because it forces
someone to have actually said something before a name falls out of the queue.

| stopReason | What it means |
|---|---|
| `said-no` | They declined, in words. The only one the prospect controls. |
| `seat-gone` | They left the role. Find the successor; the company is still live. |
| `thesis-dead` | A documented objection that kills the idea rather than defers it. Rohlig pooling cash in Germany is the model. |
| `marcel-rule` | Marcel excluded the person or the company. |
| `out-of-icp` | No US entity, no exposure, or below the band. |
| `client` | Already ours. |

**These are not stops**, however they are phrased: no reply after three touches,
unresponsive, no result, over-touched, a polite non-answer, a reply that went
nowhere. Every one of those was found in the book on 2026-10-01 doing duty as a
stop, and every one was reversed.

A reply of any kind is engagement, not an exit. Eddie Romero answered once in
May and was filed under do-not-contact in September for going quiet afterwards.
That was the worst call of the thirteen.

### Putting someone back

Set `cadenceRestart` to today and leave `touchCount` at what they actually
spent. The clock runs from the restart; the count remembers where they left off,
so a prospect resumes at touch 5 rather than being sent touch 2 again. Where
`touchCount` and the itemized `touches` list disagree, the script takes whichever
is further along: trusting the shorter record would re-send a touch the person
has already had.

### Writing a touch that is not the last one

A message that ends "I am not writing to ask again" or "you know where I am"
spends a touch and closes the sequence in the same breath. Every touch carries
an ask. Where the previous ask has been ignored more than once, change the ask
rather than repeating it, and prefer a smaller one: a yes or no question, a
single number they can check themselves, or the question of whether they are
even the right person. That last one is the most useful move at touch 4 and
beyond, because persistent silence usually means it is not their decision rather
than that they are not interested, and it gives them an easy reply that still
advances us.

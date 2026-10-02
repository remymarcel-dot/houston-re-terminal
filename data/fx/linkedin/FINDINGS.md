# What the LinkedIn archive says

Source: Marcel Remy's own LinkedIn data export, pulled 2026-09-18.
Nine files. Connections (22,536), Invitations (5,557), messages (24,309),
Reactions, Comments, Shares, Member_Follows, Hashtag_Follows, Receipts.

Derived files in this folder are screened outputs. The raw export is not
committed: it holds private message content and third party contact details.

## The one number that matters

Of the 1,766 people who accepted an invitation in 2026:

| | count | share |
|---|---|---|
| accepted | 1,766 | |
| ever messaged afterwards | 398 | 22.5% |
| ever replied | 83 | 4.7% |
| replied, of those actually messaged | 83 of 398 | **20.9%** |

**1,368 people accepted a connection request and were never sent a single
message.** The reply rate when Marcel does write is 20.9%, which is strong.
The network is not the constraint and the copy is not the constraint. The
constraint is that the network gets built and then never gets spoken to.

At his own 20.9% rate, the 1,368 unspoken-to connections are worth roughly
280 conversations, and they need no invitation because they are already
first degree.

## Connection notes: the template was the problem, not the note

Acceptance on 2026 outgoing invitations, by month:

| month | with a note | without a note |
|---|---|---|
| Jan | 323 sent, 5.0% | 111 sent, 3.6% |
| Feb | 345 sent, 5.8% | 245 sent, 4.9% |
| Mar | 62 sent, 3.2% | 665 sent, 42.7% |
| Apr | 0 | 773 sent, 53.7% |
| May | 0 | 790 sent, 36.3% |
| Jun | 0 | 518 sent, 38.6% |
| Jul | 8 sent, 25.0% | 474 sent, 33.3% |
| Aug | 76 sent, 22.4% | 783 sent, 31.9% |
| Sep | 52 sent, 17.3% | 259 sent, 34.7% |

The Jan and Feb notes were one mass template ("Always great to meet a fellow
UT Dallas alum"), 668 of them, at about 5%. That is the same 5.6% the
HeyReach campaign produced, and it is the template, not the act of writing.
Hand written notes in Jul to Sep recover to 17 to 25%.

No-note invitations still beat noted ones, and the usual explanation, that
blank invites go to easy warm contacts, does not hold here: 60 to 67% of the
March to June acceptances were CFOs, presidents, controllers and owners. He
was aiming at the right people and sending nothing.

Honest limit: this compares months, not a controlled test. Targeting changed
at the same time the notes stopped. Treat it as strong evidence against the
template and as a reason to test blank invites against hand written ones on
the same segment, not as proof that notes always hurt.

## Volume risk

5,484 outgoing invitations in 2026, 790 in May alone, roughly 180 a week.
That sits at the edge of what LinkedIn tolerates before restricting an
account. The config file caps connection requests at 15 a day for this
reason. Nothing in the archive shows a restriction, but the exposure is real.

## Files

| file | what it is |
|---|---|
| `targets-tier-a.csv` | 45 finance decision makers, FX sector, US looking, first degree, never messaged, not in pipeline |
| `targets-tier-b.csv` | 579 next best, same screen with a weaker sector or geography signal |
| `warm-dormant.csv` | 113 who replied at least once and went quiet, vendors pitching Marcel removed by hand |
| `unanswered-signals.csv` | 11 who gave a phone, an email or a yes with no LinkedIn answer after it |

Screening excludes Monex colleagues, FX and payments competitors, recruiters,
coaches and vendors, the Seidor and SAP era, and large enterprises that run
their own treasury desk and already have bank FX lines.

## What each export was worth

- **Connections** and **messages**: the two that matter. Together they give
  company, title and full conversation history, and the message archive
  reaches back to 2011, which closes the gap HeyReach cannot see before
  2026-07-30.
- **Invitations**: the acceptance analysis above.
- **Member_Follows**: 2,125 names with no company or title. Thin on its own.
- **Comments**, **Reactions**, **Shares**: engagement history, useful later
  for warm openers, not for targeting.
- **Hashtag_Follows**: 45 tags, all 2019 to 2021, entirely SAP and Seidor
  era. Stale, no value for FX work.
- **Receipts**: LinkedIn billing only. No lead value. Note that it carries
  names other than Marcel's, a leftover of corporate billing at Seidor.

## Where the lists live

The four screened CSVs are written to `data/fx/linkedin/local/`, which is
gitignored. They carry names, titles and profile URLs for several hundred
people taken from a private export, so they stay on the working machine
rather than in git history. Only this aggregate analysis is committed.

Regenerate them by re-running the screen against a fresh export. Nothing
downstream depends on them being in version control: `pipeline.json` remains
the record for anyone actually being worked.


## Correction: what "unanswered" actually means

The 11 in `unanswered-signals.csv` are threads where a buying signal is the
last thing visible on LinkedIn. That is not the same as a dropped ball, and
checking the first four proved it:

| | what the archive showed | what actually happened |
|---|---|---|
| Door Capital Partners, Alejandro Arregui | email handed over, thread ends | call took place Jan 21, no FX exposure, closed |
| TA Express, Jose Rene Tapia | mobile given, thread ends | followed up off platform, went nowhere, closed |
| Solve Networks, Jason Bell | emails and time slots given | still unverified |
| Grupo Palco, Carlos Palma | email given before the El Paso summit | still unverified |

Two of the four verified were already handled, so the detector runs at
roughly a 50% false positive rate on this sample. It finds where the
LinkedIn record stops, not where Marcel stopped. Marcel's real
conversations move to WhatsApp, email and phone, and none of that is
visible here.

Treat the list as a prompt to ask, never as a list of failures, and never
write to anyone on it before Marcel confirms what happened off platform.
Door Capital Partners, Alejandro Arregui is the case that proves the cost:
a reopen there would have pitched hedging to someone who had already sat
through a call and said he has no exposure.


## Correction: the 2025 date cut hid the best targets

The first screen kept only connections made in 2025 or later, assuming
anything older was Seidor and SAP era. Rebuilt without that cut, the
qualified pool goes from 2,556 to **6,090**.

More importantly it changes what the best target looks like. Across all
years, **178 people have replied to Marcel at least once and have been in
conversation since 2025**, are decision makers, and are not yet in the
pipeline. Vendors and large enterprises are excluded. Of those, 98 are open
loops where Marcel sent the last message.

These outrank every cold name. The relationship already exists, they have
already answered once, and many are the older Mexico and LATAM contacts
from before Monex.

Safer Food Services (SFS US), Humberto Martinez is the case that exposed
it: connected June 2019, agreed to a meeting twice in February 2026, and
invisible to every list because of the date filter.

### Rebuilt files

| file | what it is |
|---|---|
| `warm-replied-all-years.csv` | 178 who replied before and are active since 2025, ranked, open loops first |
| `never-messaged-fin-fx-all-years.csv` | 153 finance decision makers in FX sectors, never messaged, any year |

Work the warm file before the cold one. Screen on title, company and real
exposure. Connection date says when Marcel met someone, not whether they
are worth talking to.

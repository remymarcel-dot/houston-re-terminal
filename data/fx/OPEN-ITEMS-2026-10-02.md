# Everything open or pending, as of 2026-10-02

Computed from `pipeline.json`, 305 rows, not from memory.

---

# A. Needs Marcel's decision or hand. Nine items.

| # | Who | What is owed |
|---|---|---|
| 1 | **Jon Kimball**, Kimball Produce | A yes or no on the recommended **cut** |
| 2 | **Eyal Nahoumovich**, Gaia | Revival message **drafted and ready**, send by hand |
| 3 | **Shirley Bryson**, Reina Produce | Revival message **drafted and ready**, send by hand |
| 4 | **Noel Alvarez**, Triumph Seafood | Revival message **drafted and ready**, send by hand |
| 5 | **Maria Eugenia Chacin Robles**, Mexilink | Status is **scheduled-callback with NO DATE**. A promised callback with no date is a broken promise waiting to happen. Needs a date |
| 6 | **Clifford D'Souza**, Aptean | Status is **MEETING BOOKED with no next date**. The single most valuable row on the board and nothing is scheduled after it |
| 7 | **Daniel O'Quinn**, SciPlay | Door open, but **SciPlay was taken private**. Close it or find where he went |
| 8 | **Alejandro Arregui**, Door Capital Partners | Door open, no date, drifting |
| 9 | **Louise Lalor**, Hillside Winery | `superseded-failed-url`. Needs a real URL pasted or an explicit drop |

**Also never contacted at all, five rows:** Felix Lopez (company unknown), Marilyn
Florez-Giordano (Quality Importers), Mauro Souza (LongTail), Saif Khan (Zhone),
Walter Kealey III (Enchanting Travels). Work them or drop them.

---

# B. On the calendar and healthy

| Date | What |
|---|---|
| **Mon 5 Oct** | **Lead level verification** of campaigns 634736, 634581, 634669, 634676, 634737. Read `leadConnectionStatus` per lead. **Never `progressStats`**, it has been wrong twice. Carlos Gomes is Play 0, so read `leadMessageStatus`. Also check whether **Jose Antonio Martinez Haro's** invitation went, and re-add him if it failed |
| **Tue 6 Oct** | **Call Russell Foxx**, DXP, 9:30 to 10:30am CT. Sheet written |
| **Thu 8 Oct** | **28 emails** in `SEND-SHEET-2026-10-08.md`. Plus follow ups: Yllescas, Hillary Stroble, Grace Bravo Buenrostro, Sean Fightmaster |
| **Fri 9 Oct** | Follow ups: **Juan Cardenas**, **Tom Lyons** |
| **Mon 12 Oct** | **Jack Campbell** and **Jon Zaninovich**, held sequenced |
| **Thu 16 Oct** | Six follow ups: Fraymil Rodriguez, John P. Olivo, Patrick Gaughan, Luis Reynoso, **Gloria Mancilla**, **Rosa Duarte** |
| **Before 22 Oct** | Find who internally owns the **Tecma** relationship |
| **Week of 5 Oct** | **Luis Merjil** still owes a day |

**70 invitations are queued in campaigns** and need nothing but Monday's
verification. Seven messages are in flight the same way.

---

# C. THE REAL PROBLEM: 102 live rows carry no next date

Not stalled, not closed, just **unscheduled**, which in practice means dropped.
Breakdown:

| Count | Status | What it means |
|---|---|---|
| **24** | `message-sent` | Messaged, silent, no follow up date |
| **24** | `invitation-sent` | Invitation out, no acceptance check |
| **13** | `reconnected` | **Accepted the connection and were never progressed.** Warm inventory going cold |
| **12** | `in-cadence` | In a cadence with no next step named |
| **6** | `awaiting-reply` | Waiting on a reply with nothing scheduled |
| **5** | `live-conversation` / `channel-live` | **Avery O'Brien, Luz Rodriguez, Robert Guerrero, Carlos Palma, Fatima Morales.** Active conversations drifting |
| **1** | `MEETING BOOKED` | Clifford D'Souza, item 6 above |

**The 13 reconnected and the 5 live conversations are the expensive ones.** Those
people already said yes to something. They should not be the rows without dates.

---

# D. The screen backlog, and a gap in how screens are recorded

**64 screened names have no pipeline row:** 13 from the 1 Oct screen, 51 from the
2 Oct screen.

**That number overstates the problem and I cannot tell by how much.** Many were
rejected on purpose and correctly: Juvell O., Joan Oben and Esteban Alvarez lost
the one seat per company rule; Paulina Ascencio, Patricia Mendoza, Irasema George
and Luis Barriga were Marcel's explicit Sesajal exclusions; Lindsey Thiel was
rejected as right title wrong company; Cultivar, Dinant and Latam Doers are
companies, not people; one Edgar Gutierrez is a flagged duplicate.

**But the screens record no machine readable verdict**, so a deliberate rejection
and an oversight look identical from the file. **That is the gap.** `Sylvia Parra`
is the clearest casualty: screened on 2 Oct, flagged as needing her title resolved,
and then nothing.

**The fix, and it is cheap:** every screened name gets a verdict in the screen file,
one of `entered`, `rejected <reason>`, or `blocked <what is missing>`. Then this
check runs clean and an oversight cannot hide behind a rejection.

---

# E. Housekeeping

- **The Idiolect connector needs authorizing** before its tools work. Claude cannot
  run the sign in from this session. Do it in claude.ai connector settings.
- **Fraymil's comment play is closed**, Marcel's call, since he only reposts
  company content.
- **Gloria's HeyReach row stays Paused in 634736 permanently.** Never resume it; she
  was invited by hand and a resume would fire a second invitation.
- **Rosa Duarte must never enter a HeyReach campaign.** `get_lead` 404s on her URL.

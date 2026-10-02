# URLs needed, as of 2026-10-02

**Supersedes `urls-needed-2026-09-30.md`, which is fully resolved.** All sixteen
names on that list now have URLs and are in campaigns; it is kept only as history.

Every name below is now **in `pipeline.json`**, which was not true an hour ago.
See the note at the bottom.

---

## Group A: note written, needs a URL to send (11)

| # | name | company | seat | where | note lives in |
|---|---|---|---|---|---|
| 1 | **Jose Luis Lopez Mota** | vOfiz Inc | Managing Director | Greater Houston | `channel/houston-two-2026-10-02.md` |
| 2 | **Alfredo Amparan Garza** | Workhub Developments LLC | CFO and Co-Founder | The Woodlands TX | `channel/houston-two-2026-10-02.md` |
| 3 | **Gloria Viridiana Mancilla Palacios** | Grupo Sesajal | Director de Unidad de Negocio | San Antonio TX | `message-gloria-mancilla-2026-10-02.md` |
| 4 | **Roberto Contreras** | DC Partners / Moderno Porcelain | CEO | Greater Houston | `message-roberto-contreras-2026-10-02.md` |
| 5 | **Sarah Van Houten** | Catalina Snacks | CFO | Boulder CO | `message-sarah-van-houten-2026-10-02.md` |
| 6 | **John Larse** | Sweet Darling Sales | CEO | Aptos CA | `notes-2026-10-02-worth-a-note.md` item 20 |
| 7 | **Rosa Duarte** | California Giant Berry Farms | Accounting Manager | California | `notes-2026-10-02-worth-a-note.md` item 21 |
| 8 | **Eyal Nahoumovich** | Gaia | — | — | earlier draft |
| 9 | **Shirley Bryson** | Reina Produce | — | — | earlier draft |
| 10 | **Noel Alvarez** | Triumph Seafood Inc. | Company Owner | — | earlier draft |
| 11 | **Jon Kimball** | Kimball Produce Sales Inc. | Owner and Salesman | — | earlier draft |
| 12 | **Russell Foxx** | DXP Enterprises | Treasurer | — | earlier draft |

That is **twelve**, not eleven. Counted wrong twice today; the table is the
record, not the sentence.

**Jon Kimball of Kimball Produce is NOT John Kimble of JAKKS Pacific.** Two
different men, nearly the same name, and Kimble already has his URL and is in a
campaign. Do not merge them.

## Group B: needs a URL for a different reason (2)

| # | name | company | why |
|---|---|---|---|
| 13 | **J.D. Poole** | Scotlynn Sweet-Pac Growers | Chosen seat, **but no note written yet.** URL and a note both needed. |
| 14 | **Fraymil Rodriguez** | Exp. Group LLC | **DO NOT SEND ANYTHING.** His connect button reads "Pending", so an invitation already went from this account at an unknown date through an unidentified campaign. The URL is needed to **locate** that invitation, not to send a new one. |

**Juan Cardenas showed the same "Pending" state** on 2026-10-02 and has the same
problem. Worth a sweep of older campaigns rather than name-by-name archaeology.

---

## How to send them

Copy the URL from LinkedIn and paste it. **Never reconstruct a slug from a name.**
A guessed URL either fails or, worse, resolves to the wrong person.

All of Group A are 2nd degree, so each is a Play 4 invitation capped at **300
characters**. Every note is already inside that limit.

---

## Why this file exists, and what went wrong

Earlier today I told Marcel eleven notes were "written and sitting on URLs" and
named them. When he asked which URLs were missing, **five of the names I had
given him had no pipeline entry at all** — Gloria Mancilla, Roberto Contreras,
Sarah Van Houten, John Larse and Rosa Duarte. Their notes existed as loose
markdown files and nothing else. J.D. Poole and Fraymil Rodriguez existed only
inside a 1,000 line screen file.

**This is the exact failure I flagged this morning** after it nearly cost Grace
Bravo, Eduardo Sánchez and Tom Lyons, and then offered to fix and did not. A note
in a markdown file is not a tracked prospect. The pipeline is the only record
that gets read before a send, so anything not in it is invisible.

All fourteen are now in `pipeline.json`. Six carry
`status: draft-ready-manual-send` with `profileUrl: null`, which is the existing
convention, and Fraymil carries `invitation-pending-unlocated`, which is new and
deliberately ugly so it cannot be mistaken for a clean state.

**The standing rule, now also in icp.md: a name gets a pipeline entry the moment
a note is written for it, not when the URL arrives.**

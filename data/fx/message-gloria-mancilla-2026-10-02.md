# Gloria Viridiana Mancilla Palacios, Grupo Sesajal, San Antonio

**Marcel's decision, 2026-10-02: Sesajal goes to Gloria first.** The other four
Sesajal people stay out, including the group CFO in Guadalajara.

**BLOCKED ON A URL.** She is 2nd degree, so this is a Play 4 invitation capped at
300 characters, and HeyReach cannot hold her without a profile URL. Marcel can
send it by hand on LinkedIn today, or paste the URL and it goes into a campaign.

---

## Why her and not the group CFO

Sesajal is a Jalisco sesame and edible oils group. Five of its people surfaced in
the screen:

| Who | Where | Note |
|---|---|---|
| **Gloria Mancilla** | **San Antonio, TX** | Director de Unidad de Negocio. 15 mutuals. **Chosen.** |
| Luis Miguel Barriga | Guadalajara, MX | Group CFO. 30 mutuals. The reserve. |
| Paulina Ascencio | Zapopan, MX | Tesorería, 18 years. Mexico side. |
| Patricia Mendoza Inda | San Diego, CA | Senior accountant, Sesajal LLC. 3rd degree. |
| Irasema George | San Diego, CA | AP/AR specialist, Sesajal LLC. 3rd degree. |

Barriga is the senior seat and would decide. He also sits in Mexico. Under the
Angelina de León precedent he is reachable only with the US entity named
explicitly, and a cold approach to Guadalajara is expensive.

**Gloria is US based, senior, and unambiguous under the rule.** A business unit
director in San Antonio can introduce the group CFO far more cheaply than Marcel
can reach him cold. If she goes nowhere, Barriga is the reserve.

## The line the note turns on

She runs a business unit, not finance. So the note does not claim she sets the
rate. It says something sharper and true of every regional director under a
foreign parent: **the rate lands in her P&L whether or not she decides it.**

That is the complaint she already has and has probably never named as a currency
problem. It also makes the note answerable without her having to claim authority
she does not hold.

## What is deliberately not used

Sales Navigator flags **shared education** on her profile, and her photo is from
Wharton Executive Education while her degree is an EMBA from ITAM. **Neither is
on Marcel's record**, which shows UT Dallas and IPADE. Until we know which school
the flag refers to, the note claims no shared school. Inventing one to a Wharton
and ITAM graduate would be the kind of error that ends it.

---

## The invitation, 266 characters

> Gloria, una unidad de Grupo Sesajal operando desde San Antonio vive del lado
> estadounidense del negocio, y ahí el tipo de cambio con Jalisco aterriza en tu
> P&L aunque se decida en otro lado. Trabajo divisas y pagos internacionales en
> Monex USA. Con gusto conectamos.

Two alternates:

**279 chars, adds Texas**
> Gloria, dirigir una unidad de Grupo Sesajal desde San Antonio significa que el
> tipo de cambio entre Jalisco y la operación estadounidense aterriza en tu P&L,
> aunque se decida en otro lado. Trabajo divisas y pagos internacionales en Monex
> USA, aquí en Texas. Con gusto conectamos.

**287 chars, most explicit**
> Gloria, llevar una unidad de negocio de Grupo Sesajal desde San Antonio
> significa que el tipo de cambio entre Jalisco y el lado estadounidense aterriza
> directo en tu P&L, aunque la decisión se tome en otro lado. Trabajo divisas y
> pagos internacionales en Monex USA. Con gusto conectamos.

I would send the **266**. "Vive del lado estadounidense del negocio" does the
work of naming the US entity without the clumsiness of naming Sesajal LLC, and
leaves room for the P&L line to land.

## After she accepts

The first message asks the real question, which is the same one that went to
Agro Sevilla and would go to Barriga: **does the parent fix the settlement rate
between Jalisco and the US side, or is there room to negotiate it from here?**
Internal settlements are the one rate nobody negotiates, because it is an
internal transaction and feels like bookkeeping. The spread is just as real.

---

## 2026-10-02, FINAL ROUTE: MANUAL INVITATION

Marcel's call: "i can invite her manually if it is easier." It is, and it is also
safer, so the HeyReach route is abandoned for her.

**What to do**

1. Open `https://www.linkedin.com/in/g-v-m-p/`
2. Click **Connect**, then **Add a note**
3. Paste the text below. It is 290 characters, inside LinkedIn's 300 limit, so
   nothing gets trimmed.
4. Tell me it is sent and I will log the touch and set the follow-up.

**Note to paste (Spanish, 290 chars):**

```
Gloria, felicidades por el arranque en Temple. Una planta en Texas financiada desde Jalisco es justo donde el tipo de cambio pasa de ser tema de tesoreria a tema de presupuesto, y tu llevas compras y gastos. Trabajo divisas y pagos internacionales en Monex USA. Con gusto conectamos. Marcel
```

**Do NOT resume her in campaign 634736.** A resumed lead would try to send a
second invitation. Paused, it never fires, so leaving it alone costs nothing.
Worst case if it ever did fire: LinkedIn rejects the duplicate and HeyReach logs
`ConnectionRequestAlreadySent`, a harmless Failed row, not a double approach.

**Why the campaign route failed.** My error. To swap the note in I called
`stop_lead_in_campaign` first, assuming the lead had to be replaced. It did not:
`add_leads_to_campaign_v2` updates a queued lead's custom fields in place. And
`stop_lead_in_campaign` has no API inverse, so I could not undo the pause.
Re-adding was blocked twice: v1 returned 0 because she already exists in 634736,
and 630877 / 630953 / 628299 all carry `excludeInOtherCampaigns: true`, which her
presence in 634736 trips. After Marcel resumed her in the UI the API still read
`leadStatus: Paused` on three checks, by `profileUrl` and by `linkedinId`.

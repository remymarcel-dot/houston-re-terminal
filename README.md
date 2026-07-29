# Houston RE · Deal Terminal

A self-contained, Apple-styled deal terminal for Houston-metro wholesale real estate:
conservative flip + rental underwriting, per-deal risk grading, FEMA flood + HCAD
assessment truth-checks, and live-adjustable assumptions. One HTML file, no build step.

**Underwriting philosophy (baked in):** all-cash basis, ARVs cut 10–17% below
wholesaler claims (comp-ceiling method), 0% appreciation / 0% rent growth, low-end
rents, Harris-County taxes at post-rehab value, flood zone = automatic PASS,
title defects = HIGH RISK regardless of spread. Analysis, not investment advice.

## Run it

Any static server works:

```bash
python3 -m http.server 8080
# open http://localhost:8080
```

## Live lookups (website-only superpowers)

The **Live Lookups** panel queries public APIs directly from the browser —
these do NOT work in the Claude-artifact copy (its CSP blocks external hosts):

| Lookup | API | Key needed |
|---|---|---|
| Flood zone | Census geocoder → FEMA NFHL (`hazards.fema.gov` layer 28) | none |
| Assessed value / owner / land% | HCAD Parcels ArcGIS (`gis.hctx.net`) | none |
| Value + rent AVM | RentCast (`api.rentcast.io`) | `RENTCAST_KEY` |

## API keys — what to get and where

Set keys in `config.js` (copy from `config.example.js`; it is gitignored).
For a public deployment, do NOT ship paid keys in config.js — anyone can read them.
Use the free/keyless lookups publicly and keep keyed lookups to your local copy,
or proxy them through a serverless function with the key stored as a secret.

| Priority | Service | Cost | Sign up |
|---|---|---|---|
| 1 | RentCast — property records, value/rent AVMs, active listings | free 50 calls/mo, then ~$74/mo | https://app.rentcast.io/app/api |
| 2 | FEMA NFHL + Census geocoder | free, no key | nothing to do |
| 3 | HCAD parcels (Harris Cty assessments) | free, no key | nothing to do |
| 4 | HAR MLS via SimplyRETS or CoreLogic Trestle — the real live feed | ~$49–99/mo **+ sponsoring broker** | https://simplyrets.com — ask Dillon/Nate to sponsor |
| 5 | Rentometer Pro API — rent comps | ~$99/mo | https://www.rentometer.com/api |
| 6 | Zillow Bridge Interactive — Zestimates | gated approval | https://www.bridgedataoutput.com |
| 7 | ATTOM — deeds, pre-foreclosure, distress | enterprise ~$500+/mo | https://api.developer.attomdata.com |

## Repo layout

- `index.html` — the whole terminal (data embedded, computed client-side)
- `config.example.js` — API key template → copy to `config.js` (gitignored)
- `scripts/fema_flood.py` — address → FEMA flood zone (Census + NFHL, free)
- `scripts/hcad_lookup.py` — address → HCAD owner/land/appraised values
- `scripts/ingest_packets.py` — detect + extract wholesaler document packets from ~/Downloads

## Data updates

The deal book inside `index.html` is refreshed by a scheduled Claude Code task
(daily 8:00 AM: Gmail scan → underwrite → update DEALS array → redeploy artifact
and commit here). Deals auto-prune from view after 7 days (Houston wholesale velocity).

## Privacy note before hosting publicly

`index.html` embeds dispo agents' names/phones/emails and your underwriting
positions. A public GitHub Pages site exposes all of it. Keep the repo private and
use an access-controlled host (Cloudflare Access, Netlify password) if that matters.

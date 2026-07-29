#!/usr/bin/env python3
"""HCAD tax-assessment lookup via Harris County's public ArcGIS REST service.

No API key required. Data: parcel account, owner, state class, land/building/
total appraised + market values (latest tax year on the GIS layer).

Usage:
  python3 hcad_lookup.py 8514 Montridge            # street number + name
  python3 hcad_lookup.py 8514 Montridge 77055      # + zip to disambiguate
  python3 hcad_lookup.py --owner "SMITH JOHN"      # search by owner name

Notes:
- Harris County parcels only (HCAD). Fort Bend (77545) and Galveston (77573)
  counties have their own CADs and are not covered by this endpoint.
- Values are the appraisal roll, not sale prices. land_value >> bld_value on a
  "sold comp" usually means it traded as a teardown/new-build — not a rehab comp.
- The GIS layer lags the certified roll slightly; for protest-grade numbers
  pull the account on hcad.org.
"""
import json, sys, urllib.parse, urllib.request

BASE = "https://www.gis.hctx.net/arcgis/rest/services/HCAD/Parcels/MapServer/0/query"
FIELDS = ("acct_num,tax_year,owner_name_1,site_str_num,site_str_name,site_str_sfx,"
          "site_city,site_zip,state_class,StatedArea,Acreage,"
          "land_value,bld_value,impr_value,total_appraised_val,total_market_val")

def query(where):
    params = urllib.parse.urlencode({
        "where": where, "outFields": FIELDS, "returnGeometry": "false", "f": "json"})
    with urllib.request.urlopen(f"{BASE}?{params}", timeout=30) as r:
        return json.load(r).get("features", [])

def fmt(v):
    return f"${v:,.0f}" if isinstance(v, (int, float)) else "—"

def show(feats):
    if not feats:
        print("No parcel found. Check spelling (street name WITHOUT suffix, e.g. 'Montridge' not 'Montridge Dr').")
        return
    for f in feats[:10]:
        a = f["attributes"]
        print(f"\n{a['site_str_num']} {a['site_str_name']} {a.get('site_str_sfx') or ''}".rstrip()
              + f", {a.get('site_city') or 'HOUSTON'} {a['site_zip']}")
        print(f"  Account:        {a['acct_num']}  (tax year {a['tax_year']})")
        print(f"  Owner:          {a['owner_name_1']}")
        print(f"  State class:    {a['state_class']}  |  Area: {a.get('StatedArea')} ac")
        print(f"  Land value:     {fmt(a['land_value'])}")
        print(f"  Building value: {fmt(a['bld_value'])}")
        print(f"  APPRAISED:      {fmt(a['total_appraised_val'])}")
        print(f"  MARKET:         {fmt(a['total_market_val'])}")
        lv, tv = a.get("land_value") or 0, a.get("total_market_val") or 0
        if tv and lv / tv > 0.6:
            print("  ⚠ Land is >60% of value — if this 'sold', it likely traded as a teardown, not a rehab comp.")
    if len(feats) > 10:
        print(f"\n({len(feats)-10} more matches not shown — add a zip to narrow)")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(1)
    if args[0] == "--owner":
        show(query(f"UPPER(owner_name_1) LIKE '{args[1].upper()}%'"))
    else:
        num, name = args[0], args[1].upper()
        where = f"site_str_num={int(num)} AND UPPER(site_str_name) LIKE '{name}%'"
        if len(args) > 2:
            where += f" AND site_zip='{args[2]}'"
        show(query(where))

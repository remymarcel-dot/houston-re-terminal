#!/usr/bin/env python3
"""Address -> exact FEMA flood zone via Census geocoder + FEMA NFHL (both free, no key).

Pipeline: geocode the address (Census), then point-query FEMA's National Flood
Hazard Layer 'Flood Hazard Zones' (layer 28) at that lon/lat.

FLD_ZONE meaning:
  AE, A, AO, AH, VE, V = Special Flood Hazard Area (1% annual / 100-yr) = SFHA
      -> insurance required with a federal loan; flip/rental FLOOD AUTO-PASS.
  X with subtype "0.2 PCT ANNUAL CHANCE" = shaded X / X500 (500-yr) = moderate, NOT SFHA.
  X (no subtype) = minimal risk.
No polygon returned = outside mapped SFHA = Zone X (minimal).

Usage: python3 fema_flood.py "11515 Lockgate Ln, Houston, TX 77048"
"""
import sys, json, urllib.parse, urllib.request

UA = {"User-Agent": "Mozilla/5.0"}
GEO = "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress"
NFHL = "https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28/query"

def get(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=35))

def geocode(addr):
    q = urllib.parse.urlencode({"address": addr, "benchmark": "Public_AR_Current", "format": "json"})
    m = get(f"{GEO}?{q}")["result"]["addressMatches"]
    if not m:
        return None
    c = m[0]["coordinates"]
    return c["x"], c["y"], m[0]["matchedAddress"]

def flood(lon, lat):
    q = urllib.parse.urlencode({
        "geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint", "inSR": "4326",
        "spatialRel": "esriSpatialRelIntersects", "outFields": "FLD_ZONE,ZONE_SUBTY,SFHA_TF",
        "returnGeometry": "false", "f": "json"})
    f = get(f"{NFHL}?{q}").get("features", [])
    if not f:
        return "X", "minimal risk (outside mapped SFHA)", False
    a = f[0]["attributes"]
    z, sub = a.get("FLD_ZONE", "?"), (a.get("ZONE_SUBTY") or "").strip()
    sfha = z in ("A", "AE", "AO", "AH", "AR", "A99", "V", "VE")
    label = z + (f" ({sub})" if sub else "")
    return z, label, sfha

def lookup(addr):
    g = geocode(addr)
    if not g:
        return {"addr": addr, "error": "no geocode match"}
    lon, lat, matched = g
    z, label, sfha = flood(lon, lat)
    return {"addr": matched, "lon": lon, "lat": lat, "zone": z, "label": label,
            "sfha": sfha, "auto_pass": sfha}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    r = lookup(" ".join(sys.argv[1:]))
    if "error" in r:
        print(f"{r['addr']}: {r['error']}")
    else:
        flag = "SFHA -> FLOOD AUTO-PASS" if r["sfha"] else "not SFHA (clear)"
        print(f"{r['addr']}\n  FEMA zone: {r['label']}  ->  {flag}")

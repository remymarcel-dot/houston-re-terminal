#!/usr/bin/env python3
"""Scan Downloads for New Western / wholesaler deal packets and dump their text.

The Houston RE Terminal daily task calls this to auto-ingest any document
packet the user downloaded from the NW marketplace (or that Dillon emailed and
was saved). Marcel does the one-click download; this does everything after.

Usage:
  python3 ingest_packets.py            # list packet PDFs found, newest first
  python3 ingest_packets.py --text     # + dump extracted text of each (all pages)
  python3 ingest_packets.py --since 2  # only packets modified in last N days

Match rule: PDFs in ~/Downloads (Dropbox-mirrored) whose name contains
"Document Packet", "Property Analysis", or a street-address pattern. Extend
PATTERNS as new wholesalers send differently-named files.
"""
import sys, glob, os, re, time

DOWNLOADS = os.path.expanduser(
    "~/Library/CloudStorage/Dropbox/Mac (2)/Downloads")
# Name must contain one of these AND look like a property (street address or TX zip),
# so unrelated "Offering"/"Packet" business docs don't match.
PATTERNS = ["Document Packet", "Property Analysis", "Analysis Packet", "Deal Packet"]
ADDR_RE = re.compile(r"\b\d{2,6}\s+\w|\b77\d{3}\b|\bTX\b", re.I)

def find_packets(since_days=None):
    hits = []
    for f in glob.glob(os.path.join(DOWNLOADS, "*.pdf")):
        base = os.path.basename(f)
        if not any(p.lower() in base.lower() for p in PATTERNS):
            continue
        if not ADDR_RE.search(base):
            continue
        mtime = os.path.getmtime(f)
        if since_days is not None and (time.time() - mtime) > since_days * 86400:
            continue
        hits.append((mtime, f))
    return [f for _, f in sorted(hits, reverse=True)]

def extract(path):
    try:
        from pypdf import PdfReader
    except ImportError:
        return None, "pypdf not installed: python3 -m pip install --user pypdf"
    r = PdfReader(path)
    pages = []
    for i, pg in enumerate(r.pages):
        t = (pg.extract_text() or "").strip()
        pages.append(f"\n----- PAGE {i+1} ({'image/no-text' if not t else str(len(t))+' chars'}) -----\n{t}")
    return "".join(pages), None

if __name__ == "__main__":
    args = sys.argv[1:]
    since = None
    if "--since" in args:
        since = float(args[args.index("--since") + 1])
    packets = find_packets(since)
    if not packets:
        print("No deal packets found in Downloads.")
        sys.exit(0)
    print(f"Found {len(packets)} packet(s) in Downloads (newest first):")
    for p in packets:
        age_h = (time.time() - os.path.getmtime(p)) / 3600
        print(f"  [{age_h:5.1f}h ago] {os.path.basename(p)}")
    if "--text" in args:
        for p in packets:
            print(f"\n\n########## {os.path.basename(p)} ##########")
            text, err = extract(p)
            print(err if err else text)

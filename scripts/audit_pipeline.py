#!/usr/bin/env python3
"""
Pipeline integrity audit. Catches the ways a person gets contacted twice.

  python3 scripts/audit_pipeline.py

Checks, each one born from a real mistake:
  1 duplicate people          Luz Rodriguez was in twice, one row live
  2 one-seat collisions       TIME Manufacturing had TWO queued invitations
  3 touch-record gaps         15 rows said touchCount 2 with one record, so the
                              17 Sept message was invisible and re-sendable
  4 closed rows with a date   a contradiction that keeps dead names in sweeps
  5 note text reuse           the same note going to two different people
  6 draft for a contacted row a note ready to send to someone already written to
  7 same company, one campaign a double approach inside a single campaign
  8 meeting days              a booked meeting sharing its day with other work
"""
import json, re, sys, os, collections, hashlib

ROOT = os.path.join(os.path.dirname(__file__), '..')
PIPE = os.path.join(ROOT, 'data/fx/pipeline.json')
DEAD = {'closed', 'do-not-contact', 'relationship-only', 'customer', 'client',
        'superseded-failed-url', 'not-a-person'}
SENT = {'invitation-scheduled', 'invitation-sent', 'invitation-sent-manually',
        'message-sent', 'in-campaign', 'message-sending', 'message-scheduled'}

SUFFIX = re.compile(r'\b(cpa|mba|macc|cma|fmva|ctp|msml|jr|iii|ii|phd)\b')
CO_NOISE = re.compile(r'\b(inc|llc|ltd|corp|corporation|co|group|company|the|sa|de|cv|usa|us)\b')


def nname(n):
    n = SUFFIX.sub('', (n or '').lower())
    n = re.sub(r'[^a-z\s]', '', n)
    return ' '.join(sorted(w for w in n.split() if len(w) > 2))


def ncompany(c):
    c = CO_NOISE.sub('', (c or '').lower())
    return re.sub(r'[^a-z]', '', c)


def main():
    d = json.load(open(PIPE))
    rows = d if isinstance(d, list) else d.get('entries', d.get('leads', []))
    live = [r for r in rows if r.get('status') not in DEAD]
    problems = []

    g = collections.defaultdict(list)
    for r in rows:
        g[nname(r.get('name'))].append(r)
    for k, v in g.items():
        if len(v) > 1:
            problems.append(('duplicate-person',
                             ' || '.join(f"{x.get('name')} [{x.get('status')}]" for x in v)))

    cg = collections.defaultdict(list)
    for r in live:
        c = str(r.get('company') or '')
        if c and 'unknown' not in c.lower():
            cg[ncompany(c)].append(r)
    for k, v in cg.items():
        if len(v) > 1 and k:
            problems.append(('one-seat-collision',
                             f"{v[0].get('company')}: " +
                             ', '.join(f"{x.get('name')} ({x.get('status')})" for x in v)))

    for r in rows:
        tc, ts = r.get('touchCount') or 0, r.get('touches') or []
        if tc and ts and tc != len(ts):
            problems.append(('touch-record-gap',
                             f"{r.get('name')}: touchCount {tc}, {len(ts)} records"))
        if r.get('status') in DEAD and r.get('nextTouch'):
            problems.append(('closed-but-dated', f"{r.get('name')} -> {r.get('nextTouch')}"))
        if r.get('noteText') and (r.get('touchCount') or 0) > 0 and r.get('status') not in SENT:
            problems.append(('draft-for-contacted-row',
                             f"{r.get('name')} [{r.get('status')}] tc={r.get('touchCount')}"))

    seen = collections.defaultdict(list)
    for r in rows:
        t = (r.get('noteText') or '').strip()
        if len(t) > 40:
            seen[hashlib.md5(' '.join(t.split()[2:22]).lower().encode()).hexdigest()].append(r.get('name'))
    for k, v in seen.items():
        if len(v) > 1:
            problems.append(('note-text-reused', ', '.join(v)))

    cc = collections.defaultdict(list)
    for r in rows:
        if r.get('campaignId') and r.get('company'):
            cc[(r['campaignId'], ncompany(r['company']))].append(r.get('name'))
    for k, v in cc.items():
        if len(v) > 1:
            problems.append(('same-company-one-campaign', f"campaign {k[0]}: {', '.join(v)}"))

    days = collections.defaultdict(list)
    for r in rows:
        if r.get('nextTouch'):
            days[r['nextTouch']].append(r)
    for day, v in days.items():
        if any(x.get('status') == 'meeting-booked' for x in v) and len(v) > 1:
            problems.append(('meeting-day-not-clear',
                             f"{day} carries a booked meeting plus {len(v) - 1} other items"))

    if not problems:
        print(f"CLEAN. {len(rows)} rows, {len(live)} live. No integrity problems.")
        return 0
    byk = collections.defaultdict(list)
    for k, m in problems:
        byk[k].append(m)
    print(f"{len(problems)} PROBLEMS across {len(rows)} rows\n")
    for k in sorted(byk):
        print(f"## {k} ({len(byk[k])})")
        for m in byk[k]:
            print(f"   {m}")
        print()
    return 1


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""
Screen verdict ledger and checker.

Every name that appears in a screen file must carry a verdict. A screened name
with no verdict is an invisible prospect: it looks identical to a deliberate
rejection, so an oversight can hide behind one. That is how thirteen names
ranked "Worth an invitation" on 2026-10-01 were lost.

  build  rebuild data/fx/screen-verdicts.json from the screens and the pipeline
  check  exit non-zero and report anything that needs a human decision

Verdicts:
  entered                     has a pipeline row. The only self-healing verdict
  note-written-not-entered    a note exists but no pipeline row. ACTION NEEDED
  blocked-url                 recommended, waiting on Marcel to paste a URL. CHASE IT
  recommended-never-actioned  recommended, no note, no row, no recorded blocker. WORST CASE
  blocked-research            recommended, waiting on one fact. RESOLVE IT
  marcel-decision-needed      only Marcel can call it, usually company size
  relationship-ask-first      resolved: the play is to ask, never to pitch
  reserve                     a deliberate hold behind someone else at the same company
  rejected                    screened and declined, with the reason
  already-contacted           in flight before this screen. Do not re-approach
  channel                     a route to prospects, not a prospect
  not-a-person                a company or group captured as a profile
  duplicate                   the same person twice in one screen
  UNRESOLVED                  no verdict can be derived. NEEDS A PASS
"""
import re, json, glob, os, sys, collections

ROOT = os.path.join(os.path.dirname(__file__), '..')
PIPE = os.path.join(ROOT, 'data/fx/pipeline.json')
OUT  = os.path.join(ROOT, 'data/fx/screen-verdicts.json')
SCREENS = sorted(glob.glob(os.path.join(ROOT, 'data/fx/screen-*linkedin-batch*.md')))
NOTES   = glob.glob(os.path.join(ROOT, 'data/fx/notes-2026-*.md'))

# verdicts that need a human to do something
ACTIONABLE = {'note-written-not-entered', 'blocked-url', 'blocked-research',
              'marcel-decision-needed', 'recommended-never-actioned', 'UNRESOLVED'}


def pipeline_index():
    d = json.load(open(PIPE))
    rows = d if isinstance(d, list) else d.get('entries', d.get('leads', []))
    return {(r.get('name') or '').lower(): r for r in rows}


def match(name, idx):
    k = name.lower().strip()
    if k in idx:
        return idx[k]
    parts = [p for p in re.split(r'[\s,.]+', k) if len(p) > 2]
    for pn, r in idx.items():
        if parts and all(p in pn for p in parts[:2]):
            return r
    return None


def noted_names():
    out = set()
    for f in NOTES:
        for m in re.finditer(r'^#{2,3}\s*\d+\.\s*([^,\n]+?)(?:,|$)', open(f).read(), re.M):
            out.add(m.group(1).strip().lower())
    return out


def build():
    idx, noted, ledger = pipeline_index(), noted_names(), []
    manual = {}
    if os.path.exists(OUT):                      # keep hand-resolved verdicts
        for e in json.load(open(OUT)):
            if e.get('resolvedBy') == 'human':
                manual[(e['screen'], e['name'])] = e

    for f in SCREENS:
        txt = open(f).read()
        # a screen that says up front it has no URLs blocks everything it recommends
        no_urls = bool(re.search(r'\*\*No profile URLs\.\*\*', txt))
        base, sec = os.path.basename(f), None

        for line in txt.splitlines():
            m = re.match(r'^(#{2,4})\s+(.*)', line)
            if not m:
                continue
            lvl, t = len(m.group(1)), m.group(2).strip()
            num = re.match(r'^(\d+)\.\s*([^,\n]+?)(?:,|$)', t)
            if lvl == 2 and not num:
                sec = t
                continue
            if not num or lvl < 3:
                continue

            name = num.group(2).strip()
            row = match(name, idx)
            if (base, name) in manual and not row:
                # a hand-resolved verdict is kept ONLY while it stays true; a pipeline
                # row is proof the name was actioned and overrides it
                ledger.append(manual[(base, name)])
                continue

            if row:
                v, why = 'entered', f"pipeline status {row.get('status')}"
            elif name in ('Cultivar', 'Dinant', 'Latam Doers'):
                v, why = 'not-a-person', 'company or group name captured as a profile'
            elif 'duplicate' in t.lower():
                v, why = 'duplicate', t
            elif name.lower() in noted:
                v, why = ('note-written-not-entered',
                          'a note was written but there is no pipeline row, so nobody will ever send it')
            elif sec and 'Worth an invitation' in sec:
                v, why = (('blocked-url', 'recommended; the screen states it has no profile URLs, so this is waiting on Marcel and should be chased')
                          if no_urls else
                          ('recommended-never-actioned', f'screen section "{sec}" recommended an invitation; no note, no row, no recorded blocker'))
            elif sec and ('Cut' in sec or 'seat or the band is wrong' in sec):
                v, why = 'rejected', f'screen section "{sec}"'
            elif sec and 'Already in flight' in sec:
                v, why = 'already-contacted', f'screen section "{sec}"'
            elif sec and 'Channels' in sec:
                v, why = 'channel', f'screen section "{sec}"'
            else:
                v, why = 'UNRESOLVED', f'no pipeline row, no note, and section "{sec}" carries no verdict'

            ledger.append(dict(screen=base, name=name, section=sec,
                               verdict=v, detail=why, resolvedBy='derived'))

    json.dump(ledger, open(OUT, 'w'), indent=2, ensure_ascii=False)
    return ledger


def check(ledger=None):
    if ledger is None:
        ledger = json.load(open(OUT))
    counts = collections.Counter(e['verdict'] for e in ledger)
    print(f"{len(ledger)} screened names across {len(SCREENS)} screens\n")
    for v, n in counts.most_common():
        print(f"  {'!' if v in ACTIONABLE else ' '} {v:28} {n}")

    todo = [e for e in ledger if e['verdict'] in ACTIONABLE]
    if not todo:
        print("\nNothing owed. Every screened name carries a resolved verdict.")
        return 0

    print(f"\n{len(todo)} NEED A DECISION\n")
    for v in sorted({e['verdict'] for e in todo}):
        rows = [e for e in todo if e['verdict'] == v]
        print(f"## {v} ({len(rows)})")
        for e in rows:
            print(f"   {e['name']}  [{e['screen'].replace('screen-','').replace('-linkedin-batch.md','')}]")
        print()
    return 1


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'check'
    sys.exit(check(build()) if cmd == 'build' else check())

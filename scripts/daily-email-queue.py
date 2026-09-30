#!/usr/bin/env python3
"""Daily email queue for Marcel's FX outreach cadence.

Prints, for a given date, which prospects are due an EMAIL touch today.
Marcel sends every email by hand, so this produces the worklist, not the send.

Cadence (see .claude/skills/fx-prospecting/references/cadence.md):
  touch 1  day 0   LinkedIn
  touch 2  day 3   EMAIL
  touch 3  day 7   LinkedIn (only if the invitation was accepted)
  touch 4  day 10  call
  touch 5  day 14  EMAIL
  touch 6  day 18  LinkedIn engagement
  touch 7  day 21  call
  touch 8  day 30  EMAIL
  touch 9  day 40  EMAIL or call, the close out

Usage:  python3 scripts/daily-email-queue.py [YYYY-MM-DD]
"""
import json, sys, datetime, os, signal

EMAIL_TOUCHES = {2: 3, 5: 14, 8: 30, 9: 40}
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIPELINE = os.path.join(ROOT, "data", "fx", "pipeline.json")

STOP_OUTCOMES = {"do-not-contact", "declined", "client", "relationship"}

# Statuses that mean the nine touch cadence no longer applies: the thread is
# either live (Marcel is talking to them and writes by hand) or finished.
STOP_STATUS = {
    "do-not-contact", "closed", "customer", "client", "dormant",
    "dormant-three-touches", "final-touch", "meeting-booked", "MEETING BOOKED",
    "live-conversation", "channel-live", "owned-by-marcel", "vendor-inbound",
    "nurture-subscribed", "scheduled-callback", "door-open", "reconnected",
    "identified-not-contacted",
}

# The nine touch cadence was adopted on 2026-09-30 and applies to the September
# 2026 program onward. Anything whose first touch predates this was logged under
# the old one-and-done habit, so it gets no retroactive clock: dating touch 2
# from a first touch in 2021 would report a 268 day debt that never existed.
# Those names live in a revival pool Marcel works by choice, not by calendar.
CADENCE_EPOCH = datetime.date(2026, 9, 1)

# The day offsets above assume touch 1 was a LinkedIn invitation. Some prospects
# are email first, because they have no usable LinkedIn presence. For those,
# touch 2 at day 3 would mean emailing twice in three days with no reply in
# between, which reads as pressure rather than persistence. So no email touch is
# ever scheduled within this many days of the previous one.
MIN_EMAIL_GAP_DAYS = 7
EMAIL_CHANNELS = {"email", "email-manual"}


def load():
    with open(PIPELINE) as fh:
        return json.load(fh)


def touch_numbers(entry):
    """The touch numbers already spent. Tolerates malformed history.

    `touches` is meant to be a list of {"n": int, ...}. Older rows stored a bare
    count, and a row can carry loose strings. Anything unreadable falls back to
    touchCount, so a bad row narrows the queue rather than crashing it.
    """
    raw = entry.get("touches")
    done = set()
    if isinstance(raw, list):
        for t in raw:
            if isinstance(t, dict) and isinstance(t.get("n"), int):
                done.add(t["n"])
        if done:
            return done
        if raw:                            # a list we could not read at all
            return set(range(1, len(raw) + 1))
    elif isinstance(raw, (int, float)) and raw:
        return set(range(1, int(raw) + 1))

    count = entry.get("touchCount")
    if isinstance(count, (int, float)) and count:
        return set(range(1, int(count) + 1))
    return done


def due_email_touches(entry, today):
    """Return a list of (touch_number, due_date, days_overdue) owed today or earlier."""
    if entry.get("cadenceStop"):
        return []
    ft = entry.get("firstTouch")
    if not ft:
        return []
    try:
        start = datetime.date.fromisoformat(str(ft)[:10])
    except ValueError:
        return []
    if start > today:                      # first touch has not fired yet
        return []
    if start < CADENCE_EPOCH:              # pre cadence, no retroactive clock
        return []
    done = touch_numbers(entry)
    floor = last_email_date(entry)
    if floor:
        floor = floor + datetime.timedelta(days=MIN_EMAIL_GAP_DAYS)
    out = []
    for n, offset in sorted(EMAIL_TOUCHES.items()):
        if n in done:
            continue
        due = start + datetime.timedelta(days=offset)
        if floor and due < floor:          # too soon after the last email
            due = floor
        if due <= today:
            out.append((n, due, (today - due).days))
    return out[:1]                         # only the next one owed, never a backlog dump


def last_email_date(entry):
    """The date of the most recent email touch, if any was ever sent."""
    dates = []
    for t in (entry.get("touches") or []):
        if not isinstance(t, dict):
            continue
        if (t.get("channel") or "") not in EMAIL_CHANNELS:
            continue
        try:
            dates.append(datetime.date.fromisoformat(str(t.get("date"))[:10]))
        except (ValueError, TypeError):
            continue
    return max(dates) if dates else None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    today = datetime.date.fromisoformat(args[0]) if args else datetime.date.today()
    rows, blocked = [], []
    revival = 0

    for x in load():
        if (x.get("outcome") or "") in STOP_OUTCOMES:
            continue
        if (x.get("status") or "") in STOP_STATUS:
            continue
        ft = (x.get("firstTouch") or "")[:10]
        if ft and ft < CADENCE_EPOCH.isoformat():
            revival += 1
            continue
        owed = due_email_touches(x, today)
        if not owed:
            continue
        n, due, late = owed[0]
        target = (rows if x.get("email") else blocked)
        target.append({
            "name": x.get("name", "?"), "company": x.get("company"), "title": x.get("title"),
            "email": x.get("email"), "touch": n, "due": due.isoformat(), "late": late,
            "accuracy": x.get("contactAccuracyScore"),
            "phone": x.get("phone"), "mobile": x.get("mobile"),
            "play": x.get("play"), "campaign": x.get("campaignId"),
            "priority": x.get("priority"),
        })

    rows.sort(key=lambda r: (-r["late"], r["name"]))
    blocked.sort(key=lambda r: (-r["late"], r["name"]))
    print(f"EMAIL QUEUE FOR {today}")
    print(f"{len(rows)} to send, {len(blocked)} due but blocked for want of an address\n")

    for r in rows:
        late = f"  ({r['late']} days late)" if r["late"] else ""
        acc = f"  accuracy {r['accuracy']}" if r.get("accuracy") else ""
        print(f"TOUCH {r['touch']}  due {r['due']}{late}{acc}")
        print(f"  {r['name']} | {r['title']} | {r['company']}")
        print(f"  {r['email']}")
        if r.get("phone") or r.get("mobile"):
            print(f"  phone {r.get('phone') or '-'}   mobile {r.get('mobile') or '-'}")
        print()

    if blocked:
        tier1 = [r for r in blocked if (r.get("priority") or "") == "tier-1"]
        print(f"ENRICHMENT GAP: {len(blocked)} are due an email and have no address.")
        if tier1:
            print(f"The {len(tier1)} tier 1 among them, worth a ZoomInfo run first:")
            for r in tier1:
                print(f"  touch {r['touch']}  due {r['due']}  {r['name']} | {r['company']}")
        else:
            print("  None of them are tier 1. Run the full list at pace, not today.")
        print(f"  Full list:  python3 {os.path.relpath(__file__, ROOT)} {today} --gap")
        print()

    if revival:
        print(f"REVIVAL POOL: {revival} older names sit outside the cadence clock "
              f"(first touch before {CADENCE_EPOCH}). Worked by choice, not by calendar.")


def gap(today):
    """The full enrichment backlog, printed only when asked for."""
    out = []
    for x in load():
        if (x.get("outcome") or "") in STOP_OUTCOMES:
            continue
        if (x.get("status") or "") in STOP_STATUS:
            continue
        if x.get("email"):
            continue
        if not due_email_touches(x, today):
            continue
        out.append(x)
    out.sort(key=lambda x: ((x.get("priority") or "zz"), x.get("firstTouch") or "", x.get("name", "")))
    print(f"ENRICHMENT BACKLOG AS OF {today}: {len(out)} names owed an email with no address\n")
    for x in out:
        tier = x.get("priority") or "untiered"
        print(f"  [{tier}] {x.get('name')} | {x.get('company')} | {x.get('title') or '-'}")


if __name__ == "__main__":
    # Being piped into head or less should not print a traceback.
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    if "--gap" in sys.argv:
        args = [a for a in sys.argv[1:] if not a.startswith("--")]
        gap(datetime.date.fromisoformat(args[0]) if args else datetime.date.today())
    else:
        main()

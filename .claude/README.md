# Project skills

## linkedin-skills (vendored)

Twelve LinkedIn content skills vendored from
[sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills)
(MIT, see `LINKEDIN_SKILLS_LICENSE`).

- Upstream version: `1.0.26`
- Upstream commit: `a418e725c4585db9bfcc553875b70a979459d88f`

### Layout

| Path | What it is |
| --- | --- |
| `skills/linkedin-*/` | One directory per skill, each with its own `references/` |
| `references/` | Shared references the skills reach via `../../references/` |
| `lib/` | Python helpers (Apify / Publora / Pixfaro clients, URL parser) |
| `scripts/post_comment.py` | CLI helper for posting a comment |
| `requirements.txt` | `requests`, `python-dotenv` — only needed for the Python helpers |
| `.env.example` | Template for the optional API tokens |

### Skills

`linkedin-marketing` is the router; it points at the right one of:

`linkedin-post-writer`, `linkedin-comment-drafter`, `linkedin-reply-handler`,
`linkedin-humanizer`, `linkedin-hook-extractor`, `linkedin-content-planner`,
`linkedin-repurposer`, `linkedin-profile-optimizer`, `linkedin-thread-monitor`,
`linkedin-engager-analytics`, `linkedin-employee-advocacy`.

### Optional API keys

Every skill drafts and audits without any keys. Keys only unlock the
read/publish paths, and each one degrades to "paste it in yourself":

| Variable | Unlocks | Without it |
| --- | --- | --- |
| `APIFY_TOKEN` | Reading LinkedIn posts, comments, and engagers by URL | Paste the post text |
| `PUBLORA_API_KEY` + `LINKEDIN_PLATFORM_ID` | Publishing on approval | Copy the approved draft into LinkedIn |
| `PIXFARO_API_KEY` | Generating post illustrations | It drafts the image prompt only |

Copy `.env.example` to `.env` (already gitignored) to set them.

### Updating

Re-copy from upstream, keeping this layout: `skills/` flattened into
`.claude/skills/`, the bundle-root `SKILL.md` placed at
`.claude/skills/linkedin-marketing/SKILL.md` with its `references/` and
`lib/` paths rewritten to `../../`. Upstream's own `CLAUDE.md` / `AGENTS.md`
are deliberately not vendored — they are instructions for agents working on
*that* repo, not this one.

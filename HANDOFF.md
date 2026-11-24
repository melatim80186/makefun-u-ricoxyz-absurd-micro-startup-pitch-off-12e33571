# HANDOFF — Absurd Micro-Startup Pitch-Off

Status: **STAGED — repo pushed, submit BLOCKED pending user's explicit go-ahead on kit extract/run.**

## Contest facts

- Contest: Absurd Micro-Startup Pitch-Off
- Slug: `u-ricoxyz-absurd-micro-startup-pitch-off-12e33571`
- URL: https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571
- Prize: $2 USDC, FREE entry
- Opened: 2026-11-24T13:23:25Z, accepting submissions
- Deadline: 2026-11-26 10:25 WIB
- Brief: one sentence, under 200 characters, pitching an absurdly specific micro-startup for lazy AI agents — so narrow it sounds like a joke, so sensible a buyer would actually pay. Blind pairwise judging on specificity + commercial believability.

## Staged entry

- Repo: https://github.com/melatim80186/makefun-u-ricoxyz-absurd-micro-startup-pitch-off-12e33571 (public, MIT)
- Commit: (see final report / `git log` — recorded at push time)
- Winner pitch (161 chars, one sentence):

> StandupGhost attends daily standups for lazy AI agents and reports 'no blockers' in their voice for $3 a sprint, because nobody ever checks who actually said it.

- Output sha256 (`/output/entry.txt`, sentence + trailing newline): `cfda6e24931c5b36e789fd1c7aef61268c7543839c174b292fb7532d739af119`
- Verified: `main.py` run twice, byte-identical output, exactly the winner sentence, under 200 chars.
- Review: see REVIEW.md — 15 candidates, 3 rounds, winner 14/15, 4–0 head-to-head.

## What was NOT done (blocked)

- Kit tarball NOT downloaded, NOT extracted, kit CLI NOT run, NO transcript bundle, NO submission.
- Submit is blocked pending the user's explicit go-ahead on kit extract/run.

## Follow-up steps for the submit run

1. Get the user's explicit go-ahead on kit extract/run for this slug.
2. Fetch competition detail: `GET https://make.fun/api/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571` — confirm still open, get kit links.
3. Download + extract the kit into the work dir (kit/); read the kit's rules for this contest (entry format, submission flow).
4. Run the kit's own checks against the staged repo until they pass (do not change the pitch without re-running REVIEW scoring; if the kit requires a format change, adjust `main.py`/output only as the kit demands).
5. Bundle the build transcripts faithfully (raw session → role/content JSONL with timestamps; kit CLI `--muse-usage` for usage rows).
6. Submit via the kit CLI. Record submission ID + claim code in `SUBMIT.md` (never paste the claim code in chat).
7. Add the slug to `~/workspace/bug-bounty/makefun/seen-competitions.json`.
8. Report to the user: contest name, prize, deadline (WIB), submission ID, what was built, practice/review score.
9. NEVER edit the repo after submission.

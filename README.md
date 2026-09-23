# Robots.txt Competitors Watch

Daily snapshots of `robots.txt` for Studocu and its main competitors, used for GEO / AI-crawler monitoring (tracking when sites block or allow bots like GPTBot, ClaudeBot, CCBot, Google-Extended, PerplexityBot, Applebot-Extended).

## Tracked domains
- studocu.com
- chegg.com
- quizlet.com
- coursehero.com
- scribd.com
- brainly.com

## Structure
`snapshots/<YYYY-MM-DD>/<domain>.txt` — one file per domain per day. `changelog/<domain>.md` — per-domain, change-only log; a dated entry is added only when that domain's robots.txt actually changed since its last known-good snapshot.

## How it's fetched
- **Automated daily** — a cloud routine fetches via WebFetch, cron 7:00 UTC. Works even if your laptop is off. Some domains run bot/WAF protection that can block this on any given day — expected, not a bug.
- **On-demand, full 6/6 coverage** — `scripts/fetch_robots.py` (Playwright driving the real installed Chrome, headed mode), run locally when asked. Gets past the bot protection that blocks the automated fetch. Run it with:
  ```bash
  python3 scripts/fetch_robots.py https://www.chegg.com/robots.txt
  ```

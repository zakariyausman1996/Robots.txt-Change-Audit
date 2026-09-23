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
Each run writes to `snapshots/<YYYY-MM-DD>/<domain>.txt`. Diff any two dates with:

```bash
diff snapshots/2026-09-23/chegg.com.txt snapshots/2026-09-24/chegg.com.txt
```

## Known issues
- `quizlet.com` returned an HTML captcha/WAF challenge page instead of robots.txt on 2026-09-23 (bot detection). Needs a browser-based fetch or different user-agent/retry strategy to get a clean snapshot.

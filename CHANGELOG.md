# Changelog

## 2026-09-23

No changes detected. Checked: studocu.com, chegg.com, quizlet.com, coursehero.com, scribd.com, brainly.com.

An earlier run today hit an egress block on studocu.com, chegg.com, coursehero.com,
and scribd.com from its sandbox and left those snapshots untouched. A follow-up run
successfully fetched all 6 domains directly:

- studocu.com, chegg.com, coursehero.com, brainly.com: fetched successfully — no changes vs. previous snapshot.
- quizlet.com: fetch failed, see snapshots/2026-09-23/quizlet.com.txt (HTTP 403 Forbidden — bot/WAF block, consistent with the known issue in README.md)
- scribd.com: fetch failed, see snapshots/2026-09-23/scribd.com.txt (returned a bot-detection "Client Challenge" HTML page instead of robots.txt; not a network egress issue)

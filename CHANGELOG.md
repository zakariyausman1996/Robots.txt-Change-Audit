# Changelog

## 2026-09-23

No changes detected in successfully-fetched robots.txt content.

- Checked: studocu.com, chegg.com, quizlet.com, coursehero.com, scribd.com, brainly.com
- brainly.com: fetched successfully — no changes vs. previous snapshot.
- studocu.com, chegg.com, coursehero.com, scribd.com: fetch failed (network egress policy blocked outbound access to these domains from this run's sandbox — `EGRESS_BLOCKED`, not a site-side change). On-disk snapshot files were left as the last known-good content rather than overwritten; no diff could be performed today. See snapshots/2026-09-23/studocu.com.txt, snapshots/2026-09-23/chegg.com.txt, snapshots/2026-09-23/coursehero.com.txt, snapshots/2026-09-23/scribd.com.txt.
- quizlet.com: fetch failed, see snapshots/2026-09-23/quizlet.com.txt (HTTP 403 WAF/bot-detection challenge, consistent with the known issue in README.md).

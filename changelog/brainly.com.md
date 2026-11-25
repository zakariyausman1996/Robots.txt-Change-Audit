# brainly.com robots.txt change log

Entries are only added when robots.txt actually changes. No entry = no change that day.

## 2026-11-25

- Major AI-crawler policy change: a new block labeled "AI training crawlers: allowed outside Q&A and textbook pages" replaces the old per-bot rules at the end of the file.
- **GPTBot** and **Applebot-Extended**: previously fully blocked site-wide (`Disallow: /`). Now **loosened** — allowed across the site except `/question/`, `/textbook-solutions*`, and the standard excluded paths (login, signup, API, etc.). This is a significant opening of AI-training access on non-Q&A content.
- **ClaudeBot**, **CCBot**, **meta-externalagent**: newly added to this block (previously not mentioned by name, so they fell under the generic `User-agent: *` rules with no restriction on Q&A/textbook pages). Now **explicitly restricted** from `/question/` and `/textbook-solutions*` specifically, in addition to the standard excluded paths.
- Net effect: Brainly is now allowing GPTBot/Applebot-Extended broader crawl access than before, while tightening ClaudeBot/CCBot/meta-externalagent's access to exclude Q&A and textbook-solution pages specifically.
- No Sitemap changes.

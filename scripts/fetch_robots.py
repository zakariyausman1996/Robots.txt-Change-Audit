#!/usr/bin/env python3
"""Fetch a robots.txt URL using a real headed Chrome browser and print its raw text.

Using a real browser (not headless, not curl/WebFetch) reliably gets past the
bot/WAF protection (PerimeterX, Cloudflare challenge, etc.) that blocks
automated fetches for some of these domains.
"""
import sys

from playwright.sync_api import sync_playwright


def main():
    if len(sys.argv) != 2:
        print("Usage: fetch_robots.py <url>", file=sys.stderr)
        sys.exit(1)
    url = sys.argv[1]

    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
        )
        context = browser.new_context()
        context.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(2000)
        text = page.evaluate("document.body.innerText")
        browser.close()

    print(text)


if __name__ == "__main__":
    main()

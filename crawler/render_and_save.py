from playwright.sync_api import sync_playwright
import os

os.makedirs("data", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    page = browser.new_page()
    print("🌐 Navigating to JioMeet Help page...")
    page.goto("https://jiomeetpro.jio.com/webhelp")
    page.wait_for_timeout(7000)  # wait for Angular to fully render
    html = page.content()

    with open("data/rendered_page.html", "w") as f:
        f.write(html)

    print("✅ Saved to data/rendered_page.html")
    browser.close()

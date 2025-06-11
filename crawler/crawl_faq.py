from playwright.sync_api import sync_playwright
import json
import os

os.makedirs("data", exist_ok=True)

def crawl_faq_live(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Use True when finalizing
        page = browser.new_page()
        print("🚀 Navigating to FAQ page...")
        page.goto(url, timeout=60000)
        page.wait_for_timeout(8000)  # wait for Angular content

        # Grab all question/answer pairs
        faq = page.evaluate("""
        () => {
            const questions = Array.from(document.querySelectorAll("div.question"));
            const answers = Array.from(document.querySelectorAll("div.answer"));
            const faq = [];

            for (let i = 0; i < questions.length; i++) {
                const q = questions[i]?.innerText?.trim();
                const a = answers[i]?.innerText?.trim();
                if (q && a) {
                    faq.push({ question: q, answer: a });
                }
            }

            return faq;
        }
        """)

        print(f"✅ Extracted {len(faq)} FAQ entries")
        browser.close()

        # Save to file
        with open("data/faq_data.json", "w") as f:
            json.dump(faq, f, indent=2, ensure_ascii=False)
        print("✅ Saved to data/faq_data.json")

if __name__ == "__main__":
    print("✅ Crawler started")
    crawl_faq_live("https://jiomeetpro.jio.com/webhelp")

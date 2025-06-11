from playwright.sync_api import sync_playwright
import json
import time

def crawl_all_topics(base_url):
    faq_data = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set True for headless
        page = browser.new_page()
        page.goto(base_url)
        print("✅ Opened Help Page")

        # Wait for sidebar to load
        page.wait_for_selector(".side-nav", timeout=10000)
        topic_links = page.query_selector_all(".side-nav li")

        print(f"📌 Found {len(topic_links)} topics")

        for i in range(len(topic_links)):
            try:
                # Re-fetch sidebar links because the DOM is refreshed
                topic_links = page.query_selector_all(".side-nav li")
                topic = topic_links[i]
                topic_text = topic.inner_text().strip()
                print(f"➡️ Clicking: {topic_text}")

                topic.click()
                page.wait_for_timeout(2000)

                content = page.query_selector("div.content")
                if content:
                    section_text = content.inner_text().strip()
                    faq_data.append({
                        "topic": topic_text,
                        "content": section_text
                    })
                else:
                    print(f"⚠️ No content found for {topic_text}")
            except Exception as e:
                print(f"❌ Error for topic {i}: {e}")

        browser.close()
    return faq_data

if __name__ == "__main__":
    print("🚀 Starting full FAQ scrape...")
    data = crawl_all_topics("https://jiomeetpro.jio.com/webhelp")

    with open("faq_data.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Done. Extracted {len(data)} FAQ sections.")

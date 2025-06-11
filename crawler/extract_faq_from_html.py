from bs4 import BeautifulSoup
import json

with open("data/rendered_page.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

cards = soup.select(".topic-card")
faq = []

for card in cards:
    title = card.select_one(".topic-title")
    desc = card.select_one(".topic-description")
    if title and desc:
        faq.append({
            "question": title.get_text(strip=True),
            "answer": desc.get_text(strip=True)
        })

with open("data/faq_data.json", "w") as f:
    json.dump(faq, f, indent=2, ensure_ascii=False)

print(f"✅ Extracted {len(faq)} entries to data/faq_data.json")

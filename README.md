# 🤖 JioMeet FAQ Chatbot

A local Retrieval-Augmented Generation (RAG) chatbot that answers queries using live FAQs from the [JioMeet Help Center](https://jiomeetpro.jio.com/webhelp).  
Built with Playwright, FAISS, HuggingFace Embeddings, and Streamlit — powered by local LLMs via Ollama.

---

## 🧠 Features

- ✅ **Automatic FAQ Scraping** using Playwright headless browser
- ✅ **Semantic Chunking & Embedding** with HuggingFace
- ✅ **Vector Search** using FAISS
- ✅ **Streamlit Web UI** for an interactive chat interface
- ✅ **Local LLM Support** (via Ollama — runs `mistral`, `llama3`, etc.)
- ✅ **Auto-refresh Pipeline** to stay synced with latest FAQs

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/tushar0612/jiomeet-faq-bot.git
cd jiomeet-faq-bot
2. Set Up Virtual Environment
bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
3. Install & Run Ollama (for Local LLM)
Install: https://ollama.com

bash
Copy
Edit
ollama serve
ollama run mistral
You can replace mistral with any supported model like llama3, phi3, etc.

💡 Workflow
Step 1: Crawl the JioMeet FAQ Page
bash
Copy
Edit
python3 crawler/render_and_save.py
Step 2: Extract FAQs from Rendered HTML
bash
Copy
Edit
python3 crawler/extract_faq_from_html.py
Step 3: Embed FAQs into FAISS Vector Store
bash
Copy
Edit
python3 embedder/embed_faq.py
Step 4: Run the Chatbot Interface
bash
Copy
Edit
streamlit run chatbot/web_ui.py
Open your browser at http://localhost:8501

🧪 Sample Questions
"How do I download the JioMeet app?"

"What is the max time limit for meetings?"

"How can I sign in on macOS?"

📁 Project Structure
bash
Copy
Edit
jiomeet-faq-bot/
├── crawler/                # Crawling logic using Playwright
│   ├── render_and_save.py
│   └── extract_faq_from_html.py
│
├── embedder/              # Vector embedding logic
│   └── embed_faq.py
│
├── chatbot/               # Chat UI and RAG pipeline
│   ├── app.py
│   └── web_ui.py
│
├── data/                  # Contains HTML, JSON, and FAISS DB
├── requirements.txt
└── README.md
🔄 Automate FAQ Updates (Optional)
You can schedule this daily via cron or GitHub Actions:

bash
Copy
Edit
python3 crawler/render_and_save.py
python3 crawler/extract_faq_from_html.py
python3 embedder/embed_faq.py
Want a GitHub Action? I can generate one.

🔧 Tech Stack
Python 3.9+

Playwright

LangChain

FAISS

HuggingFace Transformers

Streamlit

Ollama

👤 Author
Tushar Anand
Product Manager | AI Builder
🔗 LinkedIn
📧 tushar.anand@pm.me

📜 License
This project is licensed under the MIT License.

Made with 💡 by Tushar — designed for fast, private, and accurate JioMeet support.
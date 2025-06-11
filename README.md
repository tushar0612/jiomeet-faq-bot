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

### 1. Clone the repo

```bash
git clone https://github.com/tushar0612/jiomeet-faq-bot.git
cd jiomeet-faq-bot

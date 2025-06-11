from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json, os

os.makedirs("data", exist_ok=True)

with open("data/faq_data.json") as f:
    data = json.load(f)

docs = [f"Q: {item['question']}\nA: {item['answer']}" for item in data]

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.create_documents(docs)

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

db = FAISS.from_documents(chunks, embedding_model)
db.save_local("data/faq_index")

print(f"✅ Embedded {len(chunks)} chunks and saved to data/faq_index")

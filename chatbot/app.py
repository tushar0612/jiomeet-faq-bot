from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama  # or replace with a local LLM

# Load vector index
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local("data/faq_index", embedding, allow_dangerous_deserialization=True)

# Setup retriever
retriever = db.as_retriever()

# Replace below if switching to local LLM
qa_chain = RetrievalQA.from_chain_type(
    llm = Ollama(model="mistral")
    retriever=retriever
)

query = input("Ask something about JioMeet FAQ: ")
result = qa_chain.run(query)
print("🤖 Answer:", result)

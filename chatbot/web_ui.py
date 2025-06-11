import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

st.set_page_config(page_title="JioMeet FAQ Bot", page_icon="🤖")
st.title("🤖 JioMeet FAQ Chatbot")

query = st.text_input("Ask a question about JioMeet:")

if query:
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        db = FAISS.load_local("data/faq_index", embeddings, allow_dangerous_deserialization=True)
        retriever = db.as_retriever()

        llm = Ollama(model="mistral")  # Replace with "llama3" or other if needed
        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
        answer = qa_chain.run(query)

        st.markdown("### 🤖 Answer:")
        st.success(answer)

    except Exception as e:
        st.error(f"❌ Error: {e}")

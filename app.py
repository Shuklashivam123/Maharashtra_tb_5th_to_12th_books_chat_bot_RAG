from src.embeddings import download_embeddings
from src.vector_store import connect_pinecone
from src.rag_chain import create_rag_chain

from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# ----------------------------
# UI CONFIG
# ----------------------------
st.set_page_config(
    page_title="EduMind The AI Tutor",
    layout="centered"
)
st.title("🧠 Shivam's AI Learning Assistant")

st.caption(
    "Ask questions from Maharashtra State Board textbooks "
    "(Classes 6th to 12th)"

   """ ✨ Instant answers  
    🧠 AI-powered learning  
    📖 Based on textbook content"""
)

# ----------------------------
# CACHE: heavy objects only
# ----------------------------
@st.cache_resource(show_spinner="Initializing RAG system...")
def init_rag():
    embeddings = download_embeddings()

    vectorstore = connect_pinecone("textbookbot", embeddings)

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 6, "fetch_k": 30}  # optimized
    )

    return create_rag_chain(retriever)


rag_chain = init_rag()



# ----------------------------
# SESSION STATE
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# render history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])




# show only once
if len(st.session_state.get("messages", [])) == 0:
    st.info("📚 AI-powered textbook learning assistant")
    st.success("AI Tutor is Ready 🚀")

# ----------------------------
# INPUT
# ----------------------------
question = st.chat_input("Ask your question...")

if question:
    # user message
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # spinner during LLM call
    with st.spinner("Thinking..."):
        response = rag_chain.invoke({"input": question})
        answer = response.get("answer", "No response generated.")

    # assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)


# 🔥 Important changes (samajh le)
# ❌ Remove in Streamlit:
# while True
# input()
# print()
# ✅ Replace with:
# st.chat_input()
# st.chat_message()
# st.session_state
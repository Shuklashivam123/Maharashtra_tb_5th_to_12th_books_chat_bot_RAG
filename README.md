# 📚 Maharashtra Textbook Bot (RAG-based Q&A System)

A Retrieval-Augmented Generation (RAG) application that enables intelligent question-answering over Maharashtra state textbooks (5th to 12th standard). The system uses Pinecone vector database and LLMs to generate context-aware answers from PDF content.

---

## 🚀 Project Structure

```
maharashtra-textbook-bot/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── data/
│   └── textbooks/
│
├── src/
│
│   ├── config/
│   │   └── config.py
│
│   ├── ingestion/
│   │   ├── pdf_loader.py
│   │   ├── text_splitter.py
│   │   └── pipeline.py
│
│   ├── embeddings/
│   │   └── embedder.py
│
│   ├── vectorstore/
│   │   └── pinecone_store.py
│
│   ├── retrieval/
│   │   ├── retriever.py
│   │   └── reranker.py
│
│   ├── llm/
│   │   ├── llm_client.py
│   │   └── prompt_templates.py
│
│   ├── rag/
│   │   ├── chain.py
│   │   └── orchestrator.py
│
│   ├── utils/
│   │   ├── logger.py
│   │   └── helpers.py
│
│   └── __init__.py
│
├── notebooks/
└── logs/
```

---

## 🔁 System Flow

```
PDF Documents
   ↓
PDF Loader (Text Extraction)
   ↓
Text Chunking
   ↓
Embeddings Generation
   ↓
Pinecone Vector DB Storage
   ↓
Retriever (Top-K Similar Chunks)
   ↓
LLM (Context + Prompt)
   ↓
Final Answer
```

---

## 🧠 Key Components

### 📥 Ingestion Pipeline
- Load PDFs from `data/textbooks/`
- Clean and split into chunks
- Prepare structured text for embeddings

### 🔎 Pinecone Vector DB
- Stores embeddings of textbook chunks
- Enables fast semantic similarity search

### 🤖 RAG Pipeline
- Retrieves relevant chunks from Pinecone
- Sends context to LLM
- Generates accurate answers

---

## ⚙️ Tech Stack

- Python
- Pinecone (Vector Database)
- OpenAI / LLM APIs
- LangChain / Custom RAG pipeline
- Streamlit / FastAPI
- PyPDF / pdfminer

---

## 📌 Features

- 📖 Chat with Maharashtra textbooks (Class 5–12)
- 🔍 Semantic search using embeddings
- 🧠 Context-aware AI answers
- ⚡ Fast retrieval using Pinecone
- 📦 Modular and scalable architecture

---

## 📈 Future Improvements

- Reranking using cross-encoders
- Multi-query retrieval for better recall
- RAG evaluation (RAGAS)
- FastAPI backend deployment
- LangGraph agent-based orchestration

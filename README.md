## Project Structure : 

### My RAG Based Project

maharashtra-textbook-bot/
│
├── app.py
│
├── requirements.txt
├── .env
├── README.md
│
├── data/
│   └── textbooks/
│
├── src/
│   │
│   ├── helper.py
│   ├── prompt.py
│   ├── pdf_loader.py
│   ├── embeddings.py
│   ├── cassandra_db.py
│   ├── rag_chain.py
│   ├── config.py
│   │
│   └── __init__.py
│
├── notebooks/
│
└── logs/


### Flow
PDFs
 ↓
Loader
 ↓
Chunking
 ↓
Embeddings
 ↓
Cassandra Vector DB
 ↓
Retriever
 ↓
LLM
 ↓
Answer
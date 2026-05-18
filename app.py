from src.embeddings import download_embeddings
from src.vector_store import connect_pinecone
from src.rag_chain import create_rag_chain

from dotenv import load_dotenv

load_dotenv()

embeddings = download_embeddings()

vectorstore = connect_pinecone(
    "textbookbot",
    embeddings
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 10,
        "fetch_k": 40
    }
)

rag_chain = create_rag_chain(retriever)

while True:

    question = input("Ask Question: ")

    if question == "exit":
        break

    response = rag_chain.invoke({
        "input": question
    })

    print("\nANSWER:\n")
    print(response["answer"])
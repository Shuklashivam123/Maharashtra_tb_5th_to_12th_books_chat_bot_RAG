from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore

def connect_pinecone(index_name, embeddings):
    
    vectorstore = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )

    return vectorstore
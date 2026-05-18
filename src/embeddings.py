from langchain_huggingface import HuggingFaceEmbeddings

def download_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    return embeddings
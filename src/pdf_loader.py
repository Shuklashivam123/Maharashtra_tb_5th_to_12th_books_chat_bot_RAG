from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def load_pdf(data_path):
    loader = PyPDFDirectoryLoader(data_path)
    docs = loader.load()
    return docs

def filter_docs(docs):
    minimal_docs = []

    for doc in docs:
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={
                    "source": doc.metadata.get("source"),
                    "page": doc.metadata.get("page")
                }
            )
        )

    return minimal_docs

def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    return splitter.split_documents(docs)
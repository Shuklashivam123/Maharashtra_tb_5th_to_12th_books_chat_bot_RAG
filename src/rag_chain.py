from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq

from src.prompt import system_prompt

def create_rag_chain(retriever):

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}")
        ]
    )

    question_answer_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    rag_chain = create_retrieval_chain(
        retriever,
        question_answer_chain
    )

    return rag_chain
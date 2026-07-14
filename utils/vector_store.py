from langchain_community.vectorstores import FAISS

def create_vector_store(chunks, embedding_model):
    """
    Create and save the FAISS vector database.
    """

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    vectorstore.save_local("faiss_index")

    return vectorstore
from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embedding_model):
    """
    Create and return a FAISS vector store.
    """

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_store


def save_vector_store(vector_store):
    """
    Save the vector store locally.
    """

    vector_store.save_local("faiss_index")


def load_vector_store(embedding_model):
    """
    Load an existing FAISS vector store.
    """

    vector_store = FAISS.load_local(
        "faiss_index",
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_store
from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from utils.embedding_model import get_embedding_model
from utils.vector_store import create_vector_store, save_vector_store


def ingest(pdf_path):

    documents = load_pdf(pdf_path)

    chunks = split_documents(documents)

    embedding_model = get_embedding_model()

    vector_store = create_vector_store(
        chunks,
        embedding_model
    )

    save_vector_store(vector_store)

    return len(documents), len(chunks)


if __name__ == "__main__":

    pages, chunks = ingest(
        "data/Employee_Handbook_Sample.pdf"
    )

    print(f"Pages: {pages}")
    print(f"Chunks: {chunks}")
from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from utils.embedding_model import get_embedding_model
from utils.vector_store import create_vector_store, save_vector_store


def ingest(pdf_files):

    all_documents = []

    for pdf_path, filename in pdf_files:

        documents = load_pdf(pdf_path, filename)

        all_documents.extend(documents)

    chunks = split_documents(all_documents)

    embedding_model = get_embedding_model()

    vector_store = create_vector_store(
        chunks,
        embedding_model
    )

    save_vector_store(vector_store)

    return len(all_documents), len(chunks)
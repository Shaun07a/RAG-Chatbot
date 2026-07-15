from langchain_community.document_loaders import PyPDFLoader
import os

def load_pdf(pdf_path, original_filename=None):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    if original_filename is None:
        original_filename = os.path.basename(pdf_path)

    # Store the original filename in metadata
    for doc in documents:
        doc.metadata["filename"] = original_filename

    return documents
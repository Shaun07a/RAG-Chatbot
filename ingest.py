from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from utils.embedding_model import get_embedding_model
from utils.vector_store import create_vector_store

print("Loading PDF...")

documents = load_pdf("data/Employee_Handbook_Sample.pdf")

print(f"Loaded {len(documents)} pages.")

print("Splitting document...")

chunks = split_documents(documents)

print(f"Created {len(chunks)} chunks.")

print("Loading embedding model...")

embedding_model = get_embedding_model()

print("Creating FAISS index...")

create_vector_store(chunks, embedding_model)

print("\nIngestion completed successfully!")
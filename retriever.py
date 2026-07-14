from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS index
vectorstore = FAISS.load_local(
    "faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)

question = input("Ask a question: ")

results = vectorstore.similarity_search(question, k=2)

for i, doc in enumerate(results):
    print(f"\nResult {i+1}")
    print("-" * 50)
    print(doc.page_content)
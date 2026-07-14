from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load document
loader = TextLoader("data/company_policy.txt")
documents = loader.load()

# Split document
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create FAISS vector store
vectorstore = FAISS.from_documents(
    documents=chunks,
    embedding=embedding_model
)

vectorstore.save_local("faiss_index")
print("Vector database created successfully!")
print(f"Total chunks stored: {vectorstore.index.ntotal}")

vectorstore = FAISS.load_local(
    "faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)

print("Loaded successfully!")
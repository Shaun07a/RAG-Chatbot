from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

# Load document
loader = TextLoader("data/company_policy.txt")
documents = loader.load()

# Split document
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

# Create embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Generate embedding for the first chunk
# embedding = embedding_model.embed_query(chunks[0].page_content)

# print(chunks[0].page_content)
# print("\nEmbedding length:", len(embedding))
# print("\nFirst 10 values:")
# print(embedding[:10])

embedding1 = embedding_model.embed_query(chunks[0].page_content)
embedding2 = embedding_model.embed_query(chunks[1].page_content)

print(len(embedding1))
print(len(embedding2))
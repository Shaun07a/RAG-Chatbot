from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load the document
loader = TextLoader("data/company_policy.txt")
documents = loader.load()

# Create the splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

# Split the document
chunks = text_splitter.split_documents(documents)

# Print each chunk
for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}")
    print("-" * 40)
    print(chunk.page_content)
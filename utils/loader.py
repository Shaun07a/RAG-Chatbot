from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/company_policy.txt")

documents = loader.load()

#print(documents)

# print(documents[0].page_content)

print(documents[0].metadata)
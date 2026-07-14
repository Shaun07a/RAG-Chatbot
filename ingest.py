from utils.pdf_loader import load_pdf

pdf_path = "data/sample.pdf"

documents = load_pdf(pdf_path)

print(f"Loaded {len(documents)} pages.\n")

print(documents[0].page_content)
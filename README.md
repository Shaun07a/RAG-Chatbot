# AI Document Assistant (RAG Chatbot)

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that allows users to upload one or more PDF documents and ask natural language questions based on their content. The application retrieves relevant information from the uploaded documents using vector embeddings and generates accurate responses using Google's Gemini LLM.

---

## Features

- Upload one or multiple PDF documents
- Extract and process PDF content automatically
- Intelligent text chunking
- Semantic search using FAISS vector database
- Hugging Face sentence-transformer embeddings
- Google Gemini LLM integration
- Maximal Marginal Relevance (MMR) retrieval
- Source citation with page numbers
- Interactive Streamlit web interface
- Multi-document knowledge base
- Chat history during the session

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- Python 3.13

### AI & Machine Learning
- Google Gemini API
- LangChain
- Hugging Face Sentence Transformers

### Vector Database
- FAISS

### PDF Processing
- PyPDFLoader

---

## Project Structure

```
RAG-Chatbot/
│
├── app.py
├── chatbot.py
├── ingest.py
├── requirements.txt
├── .env
├── README.md
│
├── data/
│   └── Uploaded PDFs
│
├── faiss_index/
│
└── utils/
    ├── embedding_model.py
    ├── llm.py
    ├── pdf_loader.py
    ├── prompt.py
    ├── splitter.py
    └── vector_store.py
```

---

## How It Works

1. Upload one or more PDF documents.
2. The documents are parsed and split into smaller chunks.
3. Each chunk is converted into vector embeddings using Hugging Face Sentence Transformers.
4. Embeddings are stored in a FAISS vector database.
5. When a user asks a question:
   - The query is converted into an embedding.
   - The most relevant chunks are retrieved using MMR.
   - Retrieved context is passed to the Gemini LLM.
6. The chatbot generates an answer based only on the retrieved document context.
7. The source document and page number are displayed alongside the answer.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

### Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GOOGLE_API_KEY=your_api_key_here
```

### Run the application

```bash
streamlit run app.py
```



---

## Example Questions

- What is the leave policy?
- What is the notice period?
- Summarize this document.
- What are the employee benefits?
- Explain the company's work-from-home policy.

---

## Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini
- FAISS
- Hugging Face Transformers
- Sentence Transformers
- PyPDF
- dotenv

---

## Future Improvements

- Conversation memory
- Streaming responses
- Support for DOCX and TXT files
- OCR support for scanned PDFs
- Multiple LLM selection
- Chat export
- Cloud deployment
- User authentication

---

## Learning Outcomes

Through this project I gained practical experience with:

- Retrieval-Augmented Generation (RAG)
- Vector databases
- Embedding models
- Prompt engineering
- Semantic search
- LangChain pipelines
- Large Language Models
- Streamlit application development
- Multi-document information retrieval

---


## Author

**Shaun Joseph**

GitHub: https://github.com/your-github-username

LinkedIn: https://linkedin.com/in/your-linkedin

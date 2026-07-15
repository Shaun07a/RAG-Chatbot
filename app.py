import streamlit as st

import tempfile
import os

from ingest import ingest



st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 PDF RAG Chatbot")

with st.sidebar:

    st.header("Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type="pdf"
    )

    process = st.button("Process Document")

    if process:

        if uploaded_file is None:
            st.warning("Please upload a PDF first.")

        else:

            with st.spinner("Processing document..."):

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as temp_pdf:

                    temp_pdf.write(uploaded_file.read())

                    temp_path = temp_pdf.name

                pages, chunks = ingest(temp_path)

                os.remove(temp_path)

            st.success(
                f"Document processed successfully!\n\nPages: {pages}\nChunks: {chunks}"
            )

st.write("Ask questions about your uploaded document.")
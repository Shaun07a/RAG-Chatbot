import streamlit as st

import tempfile
import os

from ingest import ingest

from chatbot import RAGChatbot

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chatbot" not in st.session_state:
    st.session_state.chatbot = None

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

                pages, chunks = ingest(
                    temp_path,
                    uploaded_file.name
                )

                st.session_state.chatbot = RAGChatbot()

                os.remove(temp_path)

            st.success(
                f"Document processed successfully!\n\nPages: {pages}\nChunks: {chunks}"
            )


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

question = st.chat_input("Ask a question about your PDF...")


if question:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(question)

    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            #answer = ask_question(question)

           

            if st.session_state.chatbot is None:

                answer = "Please upload and process a PDF first."

                sources = []

            else:

                answer, sources = st.session_state.chatbot.ask(question)

           

            st.markdown(answer)


            if sources:

                st.divider()

                st.markdown("**Sources**")

                shown = set()

                for source in sources:

                    item = (source["source"], source["page"])

                    if item not in shown:

                        shown.add(item)

                        st.caption(
                            f"{source['source']} (Page {source['page'] + 1})"
                        )


    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


st.write("Ask questions about your uploaded document.")
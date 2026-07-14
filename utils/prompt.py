from langchain_core.prompts import ChatPromptTemplate

def get_prompt():

    prompt = ChatPromptTemplate.from_template(
        """
You are a helpful AI assistant.

Answer the user's question ONLY using the context provided below.

If the answer is not present in the context, say:

"I couldn't find that information in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    return prompt
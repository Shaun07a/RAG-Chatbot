from langchain_core.prompts import PromptTemplate


def get_prompt():

    return PromptTemplate.from_template(
        """
You are a helpful AI document assistant.

Use ONLY the information provided in the context to answer the question.

If the answer is not present in the context, simply say:

"I couldn't find that information in the uploaded documents."

Previous Conversation:
{history}

Retrieved Context:
{context}

Current Question:
{question}

Answer:
"""
    )
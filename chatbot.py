from utils.embedding_model import get_embedding_model
from utils.vector_store import load_vector_store
from utils.llm import get_llm
from utils.prompt import get_prompt

from langchain_core.output_parsers import StrOutputParser


def ask_question(question):

    embedding_model = get_embedding_model()

    vector_store = load_vector_store(
        embedding_model
    )

    docs = vector_store.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    chain = (
        get_prompt()
        | get_llm()
        | StrOutputParser()
    )

    answer = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return answer


if __name__ == "__main__":

    while True:

        question = input("Ask: ")

        if question.lower() == "exit":
            break

        print(ask_question(question))
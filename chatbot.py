from utils.embedding_model import get_embedding_model
from utils.llm import get_llm
from utils.prompt import get_prompt

from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser


def load_vector_store():
    embedding_model = get_embedding_model()

    vector_store = FAISS.load_local(
        "faiss_index",
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_store


def main():

    print("=" * 60)
    print("      PDF RAG Chatbot")
    print("=" * 60)

    vector_store = load_vector_store()

    llm = get_llm()

    prompt = get_prompt()

    parser = StrOutputParser()

    chain = prompt | llm | parser

    while True:

        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        docs = vector_store.similarity_search(question, k=3)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        answer = chain.invoke(
            {
                "context": context,
                "question": question
            }
        )

        print("\nAnswer:\n")
        print(answer)


if __name__ == "__main__":
    main()
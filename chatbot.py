from utils.embedding_model import get_embedding_model
from utils.vector_store import load_vector_store
from utils.llm import get_llm
from utils.prompt import get_prompt

from langchain_core.output_parsers import StrOutputParser


class RAGChatbot:

    def __init__(self):

        self.embedding_model = get_embedding_model()

        self.vector_store = load_vector_store(
            self.embedding_model
        )

        self.chain = (
            get_prompt()
            | get_llm()
            | StrOutputParser()
        )

    def ask(self, question):

        docs = self.vector_store.similarity_search(
            question,
            k=3
        )

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        sources = []

        for doc in docs:

            sources.append(
                {
                    "source": doc.metadata.get(
                        "filename",
                        doc.metadata.get("source", "Unknown")
                    ),
                    "page": doc.metadata.get("page", "Unknown")
                }
            )
        answer = self.chain.invoke(
            {
                "context": context,
                "question": question
            }
        )

        return answer, sources


if __name__ == "__main__":

    chatbot = RAGChatbot()

    while True:

        question = input("Ask: ")

        if question.lower() == "exit":
            break

        answer, sources = chatbot.ask(question)

        print("\nAnswer:\n")

        print(answer)

        print("\nSources:")

        for source in sources:
            print(source)
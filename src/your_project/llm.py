from langchain.chat_models import ChatAnthropic
from your_project.config import secret_key

llm = ChatAnthropic(temperature=0, anthropic_api_key=secret_key)

if __name__ == "__main__":
    from langchain.chat_models import ChatAnthropic
    from langchain.schema import AIMessage, HumanMessage, SystemMessage

    messages = [
        HumanMessage(
            content="Translate this sentence from English to French. I love programming."
        )
    ]
    print(llm(messages))
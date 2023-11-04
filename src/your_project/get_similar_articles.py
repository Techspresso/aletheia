from langchain.document_loaders import BraveSearchLoader

from your_project.get_article import get_article

api_key = "BSAt2nmuC57jmjrGEY9-JNAyAHTU6Z5"

def get_articles_on_topic(topic, count=3):
    docs = search(topic, count=count)
    urls = [doc.metadata["link"] for doc in docs]
    articles = [get_article(url) for url in urls]
    return articles


def search(topic, count=3):
    loader = BraveSearchLoader(
        query=topic, api_key=api_key, search_kwargs={"count": count}
    )
    return loader.load()

if __name__ == "__main__":
    print(get_articles_on_topic("hamas and isreal"))
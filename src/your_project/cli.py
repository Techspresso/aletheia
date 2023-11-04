from pprint import pprint
import sys
from your_project import get_similar_articles
from your_project.analysis import getArticleAnalysis, getArticleTopic
from your_project.get_article import get_article_content
from your_project.models import Article


def main():
    if len(sys.argv) > 1:
        pass
    else:
        print("Please provide a URL as a command line argument.")


def get_analysis_from_url(url):
    article = get_article_content([url])[0]
    topic = getArticleTopic(article)
    print("Topic: ", topic)
    articles = get_similar_articles.get_articles_on_topic(topic)
    # dump the content fo the articles to a file
    with open("articles.txt", "w") as f:
        for article in articles:
            f.write(article)
            f.write("\n\n")
        f.close()

    articles = [
        Article(html="", title="", summary="", content=content) for content in articles
    ]
    analyses = getArticleAnalysis(articles[0])
    # analyses = [getArticleAnalysis(article) for article in articles]
    print(analyses)


def get_articles_on_topic():
    if len(sys.argv) > 1:
        topic = sys.argv[1]
        pprint(get_similar_articles.get_articles_on_topic(topic))
    else:
        print("Please provide a URL as a command line argument.")


if __name__ == "__main__":
    url = "https://www.scientificamerican.com/article/the-science-is-clear-gun-control-saves-lives1/"
    get_analysis_from_url(url)

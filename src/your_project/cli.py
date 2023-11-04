import sys

from your_project.get_article import scrape_with_playwright, article_content_extraction_schema

def main():
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
        comparative_analysis = get_analysis(urls[0])
        print(comparative_analysis)
    else:
        print("Please provide a URL as a command line argument.")

def get_analysis(url):
    article = scrape_with_playwright([url], schema=article_content_extraction_schema)
    topic = get_topic(article)
    similar_articles = get_similar_articles(article, topic)
    analyzed_articles = analyze_articles([article, *similar_articles], topic)
    comparative_analysis = get_comparative_analysis(analyzed_articles, topic)
    return comparative_analysis


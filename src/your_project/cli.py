import sys

from your_project.get_article import scrape_with_playwright, article_content_extraction_schema

def main():
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
        extracted_content = scrape_with_playwright(urls, schema=article_content_extraction_schema)
        print(extracted_content)
    else:
        print("Please provide a URL as a command line argument.")
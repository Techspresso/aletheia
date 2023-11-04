from pprint import pprint
import sys
from your_project import get_similar_articles

def main():
    if len(sys.argv) > 1:
        pass
    else:
        print("Please provide a URL as a command line argument.")

def get_articles_on_topic():
    if len(sys.argv) > 1:
        topic = sys.argv[1]
        pprint(get_similar_articles.get_articles_on_topic(topic))
    else:
        print("Please provide a URL as a command line argument.")
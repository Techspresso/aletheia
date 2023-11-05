import pprint
from flask import Flask
from flask import request, jsonify
import json
import base64
from aletheia import get_similar_articles
from aletheia.analysis import getKeyPointsClaude, getBiasClaude, getArticleAnalysis, getArticleTopic, getAntiTopic, checkIfAnti
from aletheia.get_article import get_article_content
from aletheia.models import Article


app = Flask(__name__)

@app.route("/")
def index():
    print("Query Accepcted")
    query = request.args.get("q")
    if not query:
        return "No search query provided"
    print()

    url = base64.b64decode(query).decode() #decode later
    print("Fetching article from url: " + url + "\n")
    cur_content = get_article_content([url])[0]
    print(cur_content)
    topic = getArticleTopic(cur_content['content'])
    print("Detected topic: " + topic + "\n")
    isAnti = checkIfAnti(topic)
    if(isAnti):
        anti_topic = getAntiTopic(topic)
        print("Generated Augmented Topic: " + anti_topic + "\n")
    same_articles = get_similar_articles.get_articles_on_topic(topic, url, count=2)
    diff_articles = []
    if(isAnti):
        diff_articles = get_similar_articles.get_articles_on_topic(anti_topic, url, count=2)

    anal_json = {}
    anal_json["articles"] = []

    cur_dict = {}
    cur_dict["topic"] = topic
    cur_dict["key_points"] = getKeyPointsClaude(cur_content['content'])
    cur_dict["url"] = url
    cur_dict["title"] = cur_content['title']
    cur_dict["bias"] = getBiasClaude(cur_content['content'], topic)
    anal_json["articles"].append(cur_dict)
    print("Obtained article analysis for the original article")
    pprint.pprint(cur_dict)
    print()

    for article in same_articles:
        cur_dict = {}
        cur_dict["topic"] = topic
        cur_dict["key_points"] = getKeyPointsClaude(article['content'])
        cur_dict["url"] = article['url']
        cur_dict["title"] = article['title']
        cur_dict["bias"] = getBiasClaude(article['content'], topic)
        anal_json["articles"].append(cur_dict)
        print("Obtained article analysis:")
        pprint.pprint(cur_dict)
        print()

    for article in diff_articles:
        cur_dict = {}
        cur_dict["topic"] = anti_topic
        cur_dict["key_points"] = getKeyPointsClaude(article['content'])
        cur_dict["url"] = article['url']
        cur_dict["title"] = article['title']
        cur_dict["bias"] = getBiasClaude(article['content'], anti_topic)
        anal_json["articles"].append(cur_dict)
        print("Obtained article analysis:")
        pprint.pprint(cur_dict)
        print()

    return anal_json


        
    



     
    
    
    

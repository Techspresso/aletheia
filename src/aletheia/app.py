from flask import Flask
from flask import request, jsonify
import json
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
    url = query #decode later
    cur_content = get_article_content([url])[0]
    print(cur_content)
    topic = getArticleTopic(cur_content['content'])
    print(topic)
    isAnti = checkIfAnti(topic)
    if(isAnti):
        anti_topic = getAntiTopic(topic)
        print(anti_topic)
    same_articles = get_similar_articles.get_articles_on_topic(topic, url)
    diff_articles = []
    if(isAnti):
        diff_articles = get_similar_articles.get_articles_on_topic(anti_topic, url)

    anal_json = {}
    anal_json["articles"] = []

    cur_dict = {}
    cur_dict["topic"] = topic
    cur_dict["key_points"] = getKeyPointsClaude(cur_content['content'])
    cur_dict["url"] = url
    cur_dict["title"] = cur_content['title']
    cur_dict["bias"] = getBiasClaude(cur_content['content'], topic)
    anal_json["articles"].append(cur_dict)
    print(anal_json)
    for article in same_articles:
        cur_dict = {}
        cur_dict["topic"] = topic
        cur_dict["key_points"] = getKeyPointsClaude(article['content'])
        cur_dict["url"] = article['url']
        cur_dict["title"] = article['title']
        cur_dict["bias"] = getBiasClaude(article['content'], topic)
        anal_json["articles"].append(cur_dict)

    for article in diff_articles:
        cur_dict = {}
        cur_dict["topic"] = anti_topic
        cur_dict["key_points"] = getKeyPointsClaude(article['content'])
        cur_dict["url"] = article['url']
        cur_dict["title"] = article['title']
        cur_dict["bias"] = getBiasClaude(article['content'], anti_topic)
        anal_json["articles"].append(cur_dict)

    print("**********FKIN ANAL*********")
    print(cur_dict)


        
    



     
    
    
    

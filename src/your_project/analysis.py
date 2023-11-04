import models 
from urllib.request import urlopen
from bs4 import BeautifulSoup
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_tagging_chain, create_tagging_chain_pydantic
from langchain.chat_models import ChatAnthropic
from config import secret_key
from langchain.chat_models import ChatAnthropic
from langchain.schema import AIMessage, HumanMessage, SystemMessage

llm = ChatAnthropic(temperature=0, anthropic_api_key=secret_key)

justGetNumberText = "Please provide just the number with no explanation"

def getArticleTopic(article):
    return "AI will replace jobs"

def getAntiTopic(topic):
    return "AI will not at all replace jobs"

def getStrongTopic(topic):
    return "AI will definitely replace jobs"

def getKeyPointsClaude(text):
    leaningPrompt = [
        HumanMessage(
            content="Human: Here is an article, contained in <article> tags:" + \
                "<article>\n" + text + "</article>" + \
                "\n\nProvide a summary of the text above," + \
                "highlighting its key takeaways.\nAssistant:" 
        )
    ]
    resp = llm(leaningPrompt)
    return resp.content

def getBiasClaude(text, topic):
    antiTopic = getAntiTopic(topic)
    strongTopic = getStrongTopic(topic)
    biasPromptMessage = "Human: Here is an article, contained in <article> tags:" + \
                "<article>\n" + text + "</article>" + \
                "\n\nHow biased is the article with respect to \
                \"" + topic + "\" on a scale of 0-10, \
                \"?\nAssistant: "
    biasPrompt = [
        HumanMessage(
            content= biasPromptMessage
        )
    ]
    resp = llm(biasPrompt)

    # #TODO : FILL proper checks and processing later
    biasValPrompt = [
        HumanMessage(
            content= biasPromptMessage + resp.content + \
                    "Human: " + justGetNumberText + \
                    "Assistant: " 
        )
    ]

    valResp = llm(biasValPrompt)
    return int(valResp.content)

def getLeaningClaude(text, topic):
    antiTopic = getAntiTopic(topic)
    strongTopic = getStrongTopic(topic)
    leaningPromptMessage="Human: Here is an article, contained in <article> tags:" + \
                "<article>\n" + text + "</article>" + \
                "How strongly does the article say \
                \"" + topic + "\" on a scale of 0-10, \
                where 10 means \""  + strongTopic + "\" \
                and \"" + antiTopic + "\"?\n\n" + text 
    leaningPrompt = [
        HumanMessage(
            content= leaningPromptMessage
        )
    ]
    resp = llm(leaningPrompt)

    # #TODO : FILL proper checks and processing later
    leaningValPrompt = [
        HumanMessage(
            content= leaningPromptMessage + resp.content + \
                    "Human: " + justGetNumberText + \
                    "Assistant: " 
        )
    ]

    valResp = llm(leaningValPrompt)
    return int(valResp.content)

def getArticleAnalysis(article):
    topic = getArticleTopic(article)
    anal = ArticleAnalysis()
    anal.key_points = getKeyPointsClaude(article.text)
    anal.leaning = getLeaningClaude(article.text, topic)/10.0
    anal.bias = getBiasClaude(article.text, topic)/10.0
    return anal
    


#APE TESTING
# f = open("/usr/local/google/home/snehalreddy/hackathon/simple-python-template/src/your_project/sample.txt", "r")
# text = f.read()
# print(getKeyPointsClaude(text))
# print(getLeaningClaude(text, "AI will replace jobs"))
# print(getBiasClaude(text, "AI will replace jobs"))

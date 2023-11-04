from urllib.request import urlopen
from bs4 import BeautifulSoup
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_tagging_chain, create_tagging_chain_pydantic
from langchain.chat_models import ChatAnthropic
from aletheia.config import secret_key
from langchain.chat_models import ChatAnthropic
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_experimental.llms.anthropic_functions import AnthropicFunctions
from aletheia.models import ArticleAnalysis

llm = ChatAnthropic(temperature=0, anthropic_api_key=secret_key)

justGetNumberText = "Please provide just the number with no explanation"

justGetStatement = "Can you just give one of the statements from your answer without any explanation?\n"

negateStartStatements = ["Human: I am trying to learn english\n", \
                    "Human: I am specifically trying to learn negating statements in english.\n", \
                    "Human: Can you give some examples please?\n", \
                    "Human: Can you negate \"I am going to school\"?\n"]

def getArticleTopic(article):
    prompt_template = "Extract the concise topic from this article: {article}. Skip any premable and just specify the concise topic in one line. Write the final answer in <answer> tags."
    prompt = PromptTemplate(input_variables=["article"], template=prompt_template)
    llm = AnthropicFunctions(temperature=0, anthropic_api_key=secret_key, model_name="claude-2")
    extractor = LLMChain(llm=llm, prompt=prompt)   
    topic = extractor.predict(article=article)
    return topic

def getAntiTopic(topic):
    curContext = ""
    for statement in negateStartStatements:
        curContext+=statement
        curContext+="Assistant: "
        prompt = [
            HumanMessage(
                content=curContext 
            )
        ]
        resp = llm(prompt)
        curContext += resp.content
    curContext+="Human: Can you negate \"" + topic + "\"?\n"
    curContext+="Assistant: "
    prompt = [
        HumanMessage(
            content=curContext 
        )
    ]
    resp = llm(prompt)
    curContext += resp.content
    curContext+="Human: " + justGetStatement 
    curContext+="Assistant: "
    prompt = [
        HumanMessage(
            content=curContext 
        )
    ]
    resp = llm(prompt)
    return resp.content

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

def getLeaningClaude(text, topic, antiTopic):
    print("Anti topic: " + antiTopic)
    leaningPromptMessage="Human: Here is an article, contained in <article> tags:" + \
                "<article>\n" + text + "</article>" + \
                "How strongly does the article say \
                \"" + topic + "\" on a scale of 0-10, \
                where 10 means \""  + topic + "\" \
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
    antiTopic = getAntiTopic(topic)
    anal = {}
    anal["key_points"] = getKeyPointsClaude(article.content)
    anal["leaning"] = getLeaningClaude(article.content, topic, antiTopic)/10.0
    anal["bias"] = getBiasClaude(article.content, topic)/10.0
    return anal
    


# #APE TESTING
# f = open("/usr/local/google/home/snehalreddy/hackathon/simple-python-template/src/your_project/alien.txt", "r")
# text = f.read()
# # print(getKeyPointsClaude(text))
# print(getLeaningClaude(text, "Oumuamua and the debate over whether it could be an alien spacecraft."))
# # print(getBiasClaude(text, "AI will replace jobs"))

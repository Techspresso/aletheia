from bs4 import BeautifulSoup
from langchain.chains import create_extraction_chain
import pprint
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import AsyncChromiumLoader
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.document_transformers import BeautifulSoupTransformer
from aletheia.utils import extract_titles_from_urls
from langchain.prompts import ChatPromptTemplate
from aletheia import llm
from aletheia.models import Article

def get_title_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.find("h1").text

def get_article_content(url):
    urls = [url]
    loader = AsyncChromiumLoader(urls)
    docs = loader.load()
    bs_transformer = BeautifulSoupTransformer()
    title = get_title_from_html(docs[0].page_content)
    docs_transformed = bs_transformer.transform_documents(
        docs, tags_to_extract=["article", "h1"], unwanted_tags=["aside"]
    )

    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=80000, chunk_overlap=0
    )
    splits = splitter.split_documents(docs_transformed)
    print(f"Got article content for urls: {urls}")
    return {"content": splits[0].page_content, "url": url, "title": title}


if __name__ == "__main__":
    urls = [
        "https://www.theguardian.com/world/live/2023/oct/31/israel-hamas-war-live-updates-latest-news-today-hamas-clashes-idf-gaza-aid-plan-failure",
    ]
    content = get_article_content(urls)
    print(content)

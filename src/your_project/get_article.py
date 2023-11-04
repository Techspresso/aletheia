from langchain.chains import create_extraction_chain
import pprint
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import AsyncChromiumLoader
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.document_transformers import BeautifulSoupTransformer

from langchain.prompts import ChatPromptTemplate
from your_project import llm
from your_project.models import Article

_EXTRACTION_TEMPLATE = """Extract and save the relevant entities mentioned \
in the following passage together with their properties.

Only extract the properties mentioned in the 'information_extraction' function.

If a property is not present and is not required in the function parameters, do not include it in the output.

Passage:
{input}
{schema}
"""  # noqa: E501

article_content_extraction_schema = {
    "properties": {
        "title": {"type": "string"},
        "summary": {"type": "string"},
        "content": {"type": "string"},
    },
    "required": ["title", "summary", "content"],
}


def get_article(url):
    article = scrape_with_playwright([url], schema=article_content_extraction_schema)
    if len(article) == 0:
        return None
    return article[0]

def get_article_content(urls):
    loader = AsyncChromiumLoader(urls)
    docs = loader.load()
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(
        docs, tags_to_extract=["article", "p", "li", "h1", "h2", "h3"]
    )

    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=80000, chunk_overlap=0
    )
    splits = splitter.split_documents(docs_transformed)

    return [split.page_content for split in splits]


def extract(content: str, schema: dict):
    content = f"""
    Human: <passage>
    {content}
    </passage>

    Extract and save the relevant entities mentioned
    in the following passage together with their properties.

    Only extract the properties mentioned in the schema enclosed in the <schema> tags.

    If a property is not present and is not required in the function parameters, do not include it in the output.
    Please only output the entities and their properties in the form of a json object, not the passage itself.

    <schema>
    {schema}
    </schema>

    Assistant: {{
    """
    prompt = [HumanMessage(content=content)]
    return llm.llm(prompt)


def scrape_with_playwright(urls, schema):
    loader = AsyncChromiumLoader(urls)
    docs = loader.load()
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(
        docs, tags_to_extract=["article", "p", "li", "h1", "h2", "h3"]
    )

    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=80000, chunk_overlap=0
    )
    splits = splitter.split_documents(docs_transformed)

    articles = []
    for split in splits:
        try:
            extracted = extract(schema=schema, content=split.page_content)
            # I don't know why extraced is sometimes a dict with the results in 'item' and sometimes a list
            if isinstance(extracted, dict):
                extracted = extracted["item"]
        except Exception as e:
            print(f"Error extracting article: {split.metadata}", e)
            raise e
        articles.append(Article(html=splits[0].page_content, **extracted[0]))

    return articles


if __name__ == "__main__":
    urls = [
        "https://www.theguardian.com/world/live/2023/oct/31/israel-hamas-war-live-updates-latest-news-today-hamas-clashes-idf-gaza-aid-plan-failure",
    ]
    content = get_article_content(urls)
    print(content)

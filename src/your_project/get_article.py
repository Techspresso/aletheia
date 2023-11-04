from langchain.chains import create_extraction_chain
import pprint
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer

from your_project import llm
from your_project.models import Article

article_content_extraction_schema = {
    "properties": {
        "title": {"type": "string"},
        "summary": {"type": "string"},
        "content": {"type": "string"},
    },
    "required": ["title", "summary", "content"],
}


def extract(content: str, schema: dict):
    return create_extraction_chain(schema=schema, llm=llm.llm).run(content)


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
        except Exception as e:
            print(f"Error extracting article: {split.metadata}", e)
            continue
        articles.append(Article(html=splits[0].page_content, **extracted[0]))

    return articles


if __name__ == "__main__":
    urls = [
        "https://www.nytimes.com/2023/11/03/world/middleeast/israel-bomb-jabaliya.html",
    ]
    extracted_content = scrape_with_playwright(
        urls, schema=article_content_extraction_schema
    )
    print(extracted_content)
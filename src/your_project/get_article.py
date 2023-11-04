from langchain.chains import create_extraction_chain
import pprint
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer

from your_project import llm

article_content_extraction_schema = {
    "properties": {
        "news_article_title": {"type": "string"},
        "news_article_summary": {"type": "string"},
    },
    "required": ["news_article_title", "news_article_summary"],
}


def extract(content: str, schema: dict):
    return create_extraction_chain(schema=schema, llm=llm.llm).run(content)

def extracContent():
    from langchain.chains import LLMChain
    from langchain.llms import OpenAI
    from langchain.prompts import PromptTemplate
    _EXTRACTION_TEMPLATE = """Extract and save the relevant entities mentioned \
    in the following passage together with their properties.

    Only extract the properties mentioned in the 'information_extraction' function.

    If a property is not present and is not required in the function parameters, do not include it in the output.

    Passage:
    {input}
    """  # noqa: E501
    prompt = PromptTemplate(
        input_variables=["adjective"], template=prompt_template
    )
    llm = LLMChain(llm=OpenAI(), prompt=prompt)

def scrape_with_playwright(urls, schema):
    loader = AsyncChromiumLoader(urls)
    docs = loader.load()
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(
        docs, tags_to_extract=["span"]
    )
    print("Extracting content with LLM")

    # Grab the first 1000 tokens of the site
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=80000, chunk_overlap=0
    )
    splits = splitter.split_documents(docs_transformed)

    # Process the first split
    extracted_content = extract(schema=schema, content=splits[0].page_content)
    pprint.pprint(extracted_content)
    return extracted_content

if __name__ == "__main__":
    urls = []
    extracted_content = scrape_with_playwright(urls, schema=article_content_extraction_schema)
    print(extracted_content)
from langchain_experimental.llms.anthropic_functions import AnthropicFunctions

from aletheia.config import secret_key

llm = AnthropicFunctions(temperature=0, anthropic_api_key=secret_key)
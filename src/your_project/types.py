from dataclasses import dataclass
from typing import List

@dataclass
class Article:
    html: str
    title: str
    content: str

@dataclass
class Topic:
    topic: str

@dataclass
class ArticleAnalysis:
    article: Article
    bias: float
    key_points: List[str]
    opinions: List[str]

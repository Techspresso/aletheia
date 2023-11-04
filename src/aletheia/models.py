from dataclasses import dataclass
from typing import List

@dataclass
class Article:
    html: str
    title: str
    summary: str
    content: str

@dataclass
class Topic:
    topic: str

@dataclass
class ArticleAnalysis:
    article: Article
    leaning: float #fully supporting topic(1), against topic(0)
    bias: float #How biased towards the particular leaning (0 neutral 1 very strong)
    key_points: List[str]
    opinions: List[str]

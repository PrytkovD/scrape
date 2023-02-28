from typing import List, Optional

from pydantic import BaseModel
from datetime import datetime


class Comment(BaseModel):
    text: str


class Post(BaseModel):
    id: str
    owner_id: str
    text: str
    date: str
    view_count: Optional[int]
    comment_count: Optional[int]
    reaction_count: Optional[List[int]]
    comments: Optional[List[Comment]]


class CrawlerResponse(BaseModel):
    posts: List[Post]

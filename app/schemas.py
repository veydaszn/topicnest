from pydantic import BaseModel
from typing import List

class TopicRequest(BaseModel):
    topic: str

class TopicCard(BaseModel):
    topic: str
    definition: str
    key_points: List[str]
    example: str

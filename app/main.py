from fastapi import FastAPI
from app.schemas import TopicRequest, TopicCard
from app.card_builder import build_card

app = FastAPI(
    title="TopicNest API",
    description="Micro-learning topic card generator",
    version="1.0"
)

@app.post("/card", response_model=TopicCard)
def create_card(request: TopicRequest):
    return build_card(request.topic)

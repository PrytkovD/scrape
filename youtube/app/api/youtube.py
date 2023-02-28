from fastapi import APIRouter
from typing import List
from common.api.models import Post
import os

api_key = os.getenv('YOUTUBE_API_KEY')

router = APIRouter()


@router.get('/get/', response_model=List[Post])
async def index(source: str, limit: int = 100):
    return {'Hello': 'Youtube'}

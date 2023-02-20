from typing import List
from fastapi import APIRouter
from common.api.models import Post
import requests
import os

api_access_token = os.getenv('VK_API_ACCESS_TOKEN')
api_version = os.getenv('VK_API_VERSION')

router = APIRouter()


@router.get('/get/', response_model=List[Post])
async def get_posts(source: str, limit: int = 100):
    vk_response = requests.get("https://api.vk.com/method/wall.get",
                               params={
                                   'access_token': api_access_token,
                                   'v': api_version,
                                   'domain': source,
                                   'count': limit
                               }).json()['response']['items']
    response = []
    for item in vk_response:
        response.append(Post(
            id=item['id'],
            text=item['text'],
            date=item['date']
        ))
    return response

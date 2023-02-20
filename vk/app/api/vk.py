from fastapi import APIRouter
import requests
import os

api_access_token = os.getenv('VK_API_ACCESS_TOKEN')
api_version = os.getenv('VK_API_VERSION')

router = APIRouter()


@router.get('/get_posts/')
async def get_posts(domain: str, count: int = 100):
    data = []
    response = requests.get("https://api.vk.com/method/wall.get",
                            params={
                                'access_token': api_access_token,
                                'v': api_version,
                                'domain': domain,
                                'count': count
                            })
    data = response.json()['response']['items']
    return data

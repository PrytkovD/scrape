from typing import List
from fastapi import APIRouter
from telethon import TelegramClient
from common.api.models import Post
import os

api_id = int(os.getenv('TELEGRAM_API_ID'))
api_hash = os.getenv('TELEGRAM_API_HASH')

client = TelegramClient('session', api_id, api_hash)

router = APIRouter()


@router.get('/get/', response_model=List[Post])
async def get_posts(source: str, limit: int = 100):
    response = []
    count = 0
    async with client:
        async for message in client.iter_messages(source, limit):
            if count >= limit:
                break
            response.append(Post(
                id=message.id,
                text=message.message,
                date=message.date
            ))
            count += 1
    return response


if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_posts('me'))

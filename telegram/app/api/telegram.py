from fastapi import APIRouter
from telethon import TelegramClient
import os

api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')

router = APIRouter()


@router.get('/')
async def index():
    return {api_id: api_hash}

from fastapi import FastAPI
from api.vk import router

app = FastAPI()

app.include_router(router, prefix='/scraper/vk')

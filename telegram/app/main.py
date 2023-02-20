from fastapi import FastAPI
from api.telegram import router

app = FastAPI()

app.include_router(router, prefix='/scraper/telegram')

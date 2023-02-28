from fastapi import FastAPI
from api.youtube import router

app = FastAPI()

app.include_router(router, prefix='/scraper/youtube')

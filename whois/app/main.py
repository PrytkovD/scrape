from fastapi import FastAPI
from api.whois import router

app = FastAPI()

app.include_router(router, prefix='/whois')

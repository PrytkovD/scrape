from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from app.api.telegram import client

with client:
    client.disconnect()

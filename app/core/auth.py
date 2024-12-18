from fastapi import HTTPException, Header
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_KEY_AUTH = getenv('API_KEY_AUTH')

def get_api_key(api_key_auth: str = Header(...)):
    if api_key_auth != API_KEY_AUTH:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return api_key_auth
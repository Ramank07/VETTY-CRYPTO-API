from fastapi import HTTPException, Depends
from fastapi.security import APIKeyHeader

API_KEY = "your_api_key_here"
api_key_header = APIKeyHeader(name="X-API-Key")

async def get_current_user(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key
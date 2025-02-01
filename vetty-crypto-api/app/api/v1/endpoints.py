from fastapi import APIRouter, Depends, Query
from app.utils.pagination import paginate
from app.utils.auth import get_current_user
import requests

router = APIRouter()

COINGECKO_URL = "https://api.coingecko.com/api/v3"

@router.get("/coins")
async def list_coins(
    page_num: int = Query(1, alias="page_num"),
    per_page: int = Query(10, alias="_per_page"),
    current_user: str = Depends(get_current_user)
):
    response = requests.get(f"{COINGECKO_URL}/coins/list")
    coins = response.json()
    return paginate(coins, page_num, per_page)

@router.get("/coins/{coin_id}")
async def get_coin(coin_id: str, current_user: str = Depends(get_current_user)):
    response = requests.get(f"{COINGECKO_URL}/coins/{coin_id}")
    return response.json()

@router.get("/categories")
async def list_categories(current_user: str = Depends(get_current_user)):
    response = requests.get(f"{COINGECKO_URL}/coins/categories")
    return response.json()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.get("/version")
async def version():
    return {"version": "1.0"}
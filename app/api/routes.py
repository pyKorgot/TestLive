from fastapi import APIRouter

from app.api.enpoints import test_case

api_router = APIRouter()
api_router.include_router(test_case.router)

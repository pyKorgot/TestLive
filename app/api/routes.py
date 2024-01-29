from fastapi import APIRouter

from app.api.enpoints import test_case, test_plan, test_step

api_router = APIRouter()
api_router.include_router(test_case.router)
api_router.include_router(test_plan.router)
api_router.include_router(test_step.router)

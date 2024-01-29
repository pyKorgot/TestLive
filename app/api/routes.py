from fastapi import APIRouter

from app.api.enpoints import (bind_test_release, release, test_case, test_plan,
                              test_status, test_step)

api_router = APIRouter()
api_router.include_router(test_plan.router)
api_router.include_router(test_case.router)
api_router.include_router(test_step.router)
api_router.include_router(test_status.router)
api_router.include_router(release.router)
api_router.include_router(bind_test_release.router)

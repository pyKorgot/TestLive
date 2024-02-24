from typing import Optional

from fastapi import APIRouter, Depends
from pydantic import StrictBool
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud import crud_test_plan
from app.models.test_plan import TestPlan
from app.schemas import TestPlanCreate, TestPlanDBQuery, TestPlanUpdate, TestPlanObj

router = APIRouter(prefix='/test_plan', tags=['Test Plan'])


@router.get('/', response_model=list[TestPlanDBQuery])
async def get_test_plan(id_parent: Optional[int] = None, db: AsyncSession = Depends(get_db)):
    return await crud_test_plan.get_multi(db, TestPlan.id_parent == id_parent)


# @router.get('/test_plan_test_case')
# async def get_test_plan_case(id_parent: Optional[int], db: AsyncSession = Depends(get_db));


# @router.get('/get_all')
# async def get_all_test_plan(db: AsyncSession = Depends(get_db)):
#     all_test_plan = await crud_test_plan.get_multi(db)
#     tree = {}
#     for test_plan in all_test_plan:
#         tree[test_plan.id_test_plan] = test_plan


@router.post('/', response_model=StrictBool)
async def add_test_plan(params: TestPlanCreate, db: AsyncSession = Depends(get_db)):
    await crud_test_plan.create(db, obj_in=params)
    return True


@router.put('/{id_test_plan}', response_model=StrictBool)
async def upd_test_plan(id_test_plan: int, params: TestPlanUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud_test_plan.get(db, TestPlan.id_test_plan == id_test_plan)
    await crud_test_plan.update(db, db_obj=obj, obj_in=params)
    return True


@router.delete('/{id_test_plan}', response_model=StrictBool)
async def del_test_plan(id_test_plan: int, db: AsyncSession = Depends(get_db)):
    await crud_test_plan.remove(db, TestPlan.id_test_plan == id_test_plan)
    return True

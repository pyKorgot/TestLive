from fastapi import APIRouter, Depends
from pydantic import StrictBool
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud import crud_test_step
from app.models import TestStep
from app.schemas import TestStepCreate, TestStepDBQuery, TestStepUpdate

router = APIRouter(prefix='/test_step', tags=['Test Step'])


@router.get('/', response_model=list[TestStepDBQuery])
async def get_test_plan(id_test_case: int, db: AsyncSession = Depends(get_db)):
    return await crud_test_step.get_multi(db, TestStep.id_test_case == id_test_case)


@router.post('/', response_model=StrictBool)
async def add_test_step(params: TestStepCreate, db: AsyncSession = Depends(get_db)):
    await crud_test_step.create(db, obj_in=params)
    return True


@router.put('/{id_test_step}', response_model=StrictBool)
async def upd_test_step(id_test_step: int, params: TestStepUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud_test_step.get(db, TestStep.id_test_step == id_test_step)
    await crud_test_step.update(db, db_obj=obj, obj_in=params)
    return True


@router.delete('/{id_test_step}', response_model=StrictBool)
async def del_test_step(id_test_step: int, db: AsyncSession = Depends(get_db)):
    await crud_test_step.remove(db, TestStep.id_test_step == id_test_step)
    return True

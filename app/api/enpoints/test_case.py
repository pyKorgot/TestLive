from typing import Optional

from fastapi import APIRouter, Depends
from pydantic import StrictBool
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud.test_case import crud_test_case
from app.models import TestCase
from app.schemas import TestCaseCreate, TestCaseDBQuery, TestCaseUpdate

router = APIRouter(prefix='/test_case', tags=['Test Case'])


@router.get('/', response_model=list[TestCaseDBQuery])
async def get_test_case(id_test_plan: Optional[int] = None, db: AsyncSession = Depends(get_db)):
    res = await crud_test_case.get(db, TestCase.id_test_plan == id_test_plan)
    return res


@router.post('/', response_model=StrictBool)
async def add_test_case(params: TestCaseCreate, db: AsyncSession = Depends(get_db)):
    await crud_test_case.create(db, obj_in=params)
    return True


@router.put('/{id_test_case}', response_model=StrictBool)
async def upd_test_case(id_test_case: int, params: TestCaseUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud_test_case.get(db, TestCase.id_test_case == id_test_case)
    await crud_test_case.update(db, db_obj=obj, obj_in=params)
    return True


@router.delete('/{id_test_case}', response_model=StrictBool)
async def del_test_case(id_test_case: int, db: AsyncSession = Depends(get_db)):
    await crud_test_case.remove(db, TestCase.id_test_case == id_test_case)
    return True

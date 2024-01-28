from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud.test_case import crud_test_case
from app.models import TestCase
from app.schemas import TestCaseCreate, TestCaseBase
from sqlalchemy import text

router = APIRouter(prefix='/test_case')

@router.get('/{id_test}', response_model=list[TestCaseBase])
async def get_test(id_test: int, db: AsyncSession = Depends(get_db)):
    res = await crud_test_case.get(db, TestCase.id_test == id_test)
    return res


@router.post('/', summary='Create Test')
async def add_test(params: TestCaseCreate, db: AsyncSession = Depends(get_db)):
    test_obj = await crud_test_case.create(db, obj_in=params)
    return test_obj

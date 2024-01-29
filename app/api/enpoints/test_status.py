from fastapi import APIRouter, Depends
from pydantic import StrictBool
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud import crud_test_status
from app.models import TestStatus
from app.schemas import TestStatusCreate, TestStatusDBQuery, TestStatusUpdate

router = APIRouter(prefix='/test_status', tags=['Test Status'])


@router.get('/', response_model=list[TestStatusDBQuery])
async def get_test_status(db: AsyncSession = Depends(get_db)):
    res = await crud_test_status.get_multi(db)
    return res


@router.post('/', response_model=StrictBool)
async def add_test_status(params: TestStatusCreate, db: AsyncSession = Depends(get_db)):
    await crud_test_status.create(db, obj_in=params)
    return True


@router.put('/{id_test_status}', response_model=StrictBool)
async def upd_test_status(id_test_status: int, params: TestStatusUpdate, db: AsyncSession = Depends(get_db)):
    obj = crud_test_status.get(db, TestStatus.id_test_status == id_test_status)
    await crud_test_status.update(db, db_obj=obj, obj_in=params)
    return True


@router.delete('/{id_test_status}', response_model=StrictBool)
async def del_test_status(id_test_status: int, db: AsyncSession = Depends(get_db)):
    await crud_test_status.remove(db, TestStatus.id_test_status == id_test_status)
    return True

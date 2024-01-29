from fastapi import APIRouter, Depends
from pydantic import StrictBool
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud import crud_bind_test_release
from app.models import BindTestRelease
from app.schemas import (BindTestReleaseCreate, BindTestReleaseDBQuery,
                         BindTestReleaseUpdate)

router = APIRouter(prefix='/bind_test_release', tags=['Bind Test Release'])


@router.get('/', response_model=list[BindTestReleaseDBQuery])
async def get_bind_test_release(db: AsyncSession = Depends(get_db)):
    res = await crud_bind_test_release.get_multi(db)
    return res


@router.post('/', response_model=StrictBool)
async def add_bind_test_release(params: BindTestReleaseCreate, db: AsyncSession = Depends(get_db)):
    await crud_bind_test_release.create(db, obj_in=params)
    return True


@router.put('/{id_bind_test_release}', response_model=StrictBool)
async def upd_bind_test_release(id_bind_test_release: int, params: BindTestReleaseUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud_bind_test_release.get(db, BindTestRelease.id_bind_test_release == id_bind_test_release)
    await crud_bind_test_release.update(db, db_obj=obj, obj_in=params)
    return True


@router.delete('/{id_bind_test_release}', response_model=StrictBool)
async def del_bind_test_release(id_bind_test_release: int, db: AsyncSession = Depends(get_db)):
    await crud_bind_test_release.remove(db, BindTestRelease.id_bind_test_release == id_bind_test_release)
    return True

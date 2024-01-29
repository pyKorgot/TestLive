from fastapi import APIRouter, Depends
from pydantic import StrictBool
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud import crud_release
from app.models import Release
from app.schemas import ReleaseCreate, ReleaseDBQuery, ReleaseUpdate

router = APIRouter(prefix='/release', tags=['Release'])


@router.get('/', response_model=list[ReleaseDBQuery])
async def get_release(db: AsyncSession = Depends(get_db)):
    res = await crud_release.get_multi(db)
    return res


@router.post('/', response_model=StrictBool)
async def add_release(params: ReleaseCreate, db: AsyncSession = Depends(get_db)):
    await crud_release.create(db, obj_in=params)
    return True


@router.put('/{id_release}', response_model=StrictBool)
async def upd_release(id_release: int, params: ReleaseUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud_release.get(db, Release.id_release == id_release)
    await crud_release.update(db, db_obj=obj, obj_in=params)
    return True


@router.delete('/{id_release}', response_model=StrictBool)
async def del_release(id_release: int, db: AsyncSession = Depends(get_db)):
    await crud_release.remove(db, Release.id_release == id_release)
    return True

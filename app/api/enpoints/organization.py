from app.api.deps import get_db
from app.crud.organization import crud_organization
from app.schemas import OrganizationDBQuery, OrganizationUpdate, OrganiztionCreate
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import StrictBool
from app.models import Organization

router = APIRouter(prefix='/organization', tags=['Organization'])


@router.get('/', response_model=list[OrganizationDBQuery])
async def get_organization(db: AsyncSession = Depends(get_db)):
    res = await crud_organization.get_multi(db)
    return res


@router.post('/', response_model=StrictBool)
async def create_organization(params: OrganiztionCreate, db: AsyncSession = Depends(get_db)):
    await crud_organization.create(db, obj_in=params)
    return True


@router.put('/', response_model=StrictBool)
async def update_organization(params: OrganizationUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud_organization.get(db, Organization.id_organization == params.id_organization)
    await crud_organization.update(db, db_obj=obj, obj_in=params)
    return True


@router.delete('/', response_model=StrictBool)
async def delete_organization(id_organization: int, db: AsyncSession = Depends(get_db)):
    await crud_organization.remove(db, Organization.id_organization == id_organization)
    return True

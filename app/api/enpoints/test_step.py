from fastapi import APIRouter, Depends
from pydantic import StrictBool
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud import crud_test_step
from app.models import TestStep
from app.schemas import TestStepCreate, TestStepDBQuery, TestStepUpdate
from fastapi.encoders import jsonable_encoder


router = APIRouter(prefix='/test_step', tags=['Test Step'])


@router.get('/', response_model=list[TestStepDBQuery])
async def get_test_plan(id_test_case: int, db: AsyncSession = Depends(get_db)):
    return await crud_test_step.get_multi(db, TestStep.id_test_case == id_test_case)


@router.post('/', response_model=StrictBool)
async def add_test_step(params: list[TestStepCreate], db: AsyncSession = Depends(get_db)):
    test_step_objs = []
    for test_step in params:
        test_step_encod = jsonable_encoder(test_step)
        test_step_objs.append(TestStep(**test_step_encod))
    db.add_all(test_step_objs)
    await db.commit()
    return True


@router.put('/', response_model=StrictBool)
async def upd_test_step(params: list[TestStepUpdate], db: AsyncSession = Depends(get_db)):
    id_step_map = {step.id_test_step: step.dict() for step in params}
    ids_test_step = id_step_map.keys()

    objs = await crud_test_step.get_multi(db, TestStep.id_test_step.in_(ids_test_step))
    for obj in objs:
        if test_step := id_step_map.get(obj.id_test_step):
            for attr_name, value in test_step.items():
                setattr(obj, attr_name, value)
    await db.commit()
    return True


@router.delete('/{id_test_step}', response_model=StrictBool)
async def del_test_step(id_test_step: int, db: AsyncSession = Depends(get_db)):
    await crud_test_step.remove(db, TestStep.id_test_step == id_test_step)
    return True

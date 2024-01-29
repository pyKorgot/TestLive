from typing import Optional

from pydantic import BaseModel


class TestPlanDBQuery(BaseModel):
    id_test_plan: int
    id_parent: Optional[int]
    name: str

    class Config:
        orm_mode = True


class TestPlanCreate(BaseModel):
    name: str
    id_parent: Optional[int]


class TestPlanUpdate(BaseModel):
    name: str
    id_parent: Optional[int]

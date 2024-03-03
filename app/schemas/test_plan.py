from typing import Optional

from pydantic import BaseModel, computed_field


class TestPlanDBQuery(BaseModel):
    id_test_plan: int
    id_parent: Optional[int]
    name: str
    isLeaf: Optional[bool] = False

    @computed_field
    def key(self) -> str:
        return f'{self.id_test_plan}tp'

    class Config:
        orm_mode = True


class TestPlanCreate(BaseModel):
    name: str
    id_parent: Optional[int]


class TestPlanUpdate(BaseModel):
    name: str
    id_parent: Optional[int]

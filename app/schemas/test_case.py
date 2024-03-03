from pydantic import BaseModel, computed_field


class TestCaseDBQuery(BaseModel):
    id_test_case: int
    id_test_plan: int
    name: str
    isLeaf: bool = True

    @computed_field
    def key(self) -> str:
        return f'{self.id_test_case}tc'

    class Config:
        orm_mode = True


class TestCaseCreate(BaseModel):
    id_test_plan: int
    name: str


class TestCaseUpdate(BaseModel):
    id_test_plan: int
    name: str

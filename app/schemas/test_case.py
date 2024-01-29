from pydantic import BaseModel


class TestCaseDBQuery(BaseModel):
    id_test_case: int
    id_test_plan: int
    name: str

    class Config:
        orm_mode = True


class TestCaseCreate(BaseModel):
    id_test_plan: int
    name: str


class TestCaseUpdate(BaseModel):
    id_test_plan: int
    name: str

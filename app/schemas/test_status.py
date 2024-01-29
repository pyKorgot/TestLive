from pydantic import BaseModel


class TestStatusDBQuery(BaseModel):
    id_test_status: int
    code_status: str
    name_status: str


class TestStatusCreate(BaseModel):
    code_status: str
    name_status: str


class TestStatusUpdate(BaseModel):
    code_status: str
    name_status: str

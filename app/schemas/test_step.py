from pydantic import BaseModel


class TestStepDBQuery(BaseModel):
    id_test_step: int
    id_test_case: int

    playback: str
    excepted: str

    class Config:
        orm_mode = True


class TestStepCreate(BaseModel):
    id_test_case: int
    playback: str
    excepted: str


class TestStepUpdate(BaseModel):
    id_test_case: int
    playback: str
    excepted: str

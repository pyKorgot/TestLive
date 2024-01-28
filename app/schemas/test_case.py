from pydantic import BaseModel


class TestCaseBase(BaseModel):
    id_test: int
    playback: str
    excepted: str

    class Config:
        orm_mode = True


class TestCaseCreate(BaseModel):
    playback: str
    excepted: str


class TestCaseUpdate(BaseModel):
    playback:str
    excepted: str

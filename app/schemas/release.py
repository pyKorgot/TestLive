from pydantic import BaseModel


class ReleaseDBQuery(BaseModel):
    id_release: int
    name: str


class ReleaseCreate(BaseModel):
    name: str


class ReleaseUpdate(BaseModel):
    name: str

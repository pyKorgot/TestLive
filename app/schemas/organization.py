from pydantic import BaseModel


class OrganizationDBQuery(BaseModel):
    id_organization: int
    name_organization: str


class OrganiztionCreate(BaseModel):
    name_organization: str


class OrganizationUpdate(BaseModel):
    id_organization: int

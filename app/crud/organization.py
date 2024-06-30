from app.crud.base import CRUDBase
from app.models import Organization
from app.schemas import OrganiztionCreate, OrganizationUpdate


class CRUDBOrganization(CRUDBase[Organization, OrganiztionCreate, OrganizationUpdate]):
    pass


crud_organization = CRUDBOrganization(Organization)

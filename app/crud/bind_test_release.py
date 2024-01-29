from app.crud.base import CRUDBase
from app.models import BindTestRelease
from app.schemas import BindTestReleaseCreate, BindTestReleaseUpdate


class CRUDBindTestRelease(CRUDBase[BindTestRelease, BindTestReleaseCreate, BindTestReleaseUpdate]):
    pass


crud_bind_test_release = CRUDBindTestRelease(BindTestRelease)

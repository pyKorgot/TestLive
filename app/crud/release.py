from app.crud.base import CRUDBase
from app.models import Release
from app.schemas import ReleaseCreate, ReleaseUpdate


class CRUDRelease(CRUDBase[Release, ReleaseCreate, ReleaseUpdate]):
    pass


crud_release = CRUDRelease(Release)

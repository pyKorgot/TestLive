from app.crud.base import CRUDBase
from app.models import TestStatus
from app.schemas import TestStatusCreate, TestStatusUpdate


class CRUDTestStatus(CRUDBase[TestStatus, TestStatusCreate, TestStatusUpdate]):
    pass


crud_test_status = CRUDTestStatus(TestStatus)

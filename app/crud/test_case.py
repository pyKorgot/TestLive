from app.crud.base import CRUDBase
from app.models.test_case import TestCase
from app.schemas import TestCaseCreate, TestCaseUpdate


class CRUDTestCase(CRUDBase[TestCase, TestCaseCreate, TestCaseUpdate]):
    pass


crud_test_case = CRUDTestCase(TestCase)

from app.crud.base import CRUDBase
from app.models.test_step import TestStep
from app.schemas import TestCaseUpdate, TestStepCreate


class CRUDTestStep(CRUDBase[TestStep, TestStepCreate, TestCaseUpdate]):
    pass


crud_test_step = CRUDTestStep(TestStep)

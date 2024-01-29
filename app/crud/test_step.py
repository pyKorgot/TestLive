from app.crud.base import CRUDBase
from app.models.test_plan import TestPlan
from app.models.test_step import TestStep
from app.schemas import (TestCaseUpdate, TestPlanCreate, TestPlanUpdate,
                         TestStepCreate)


class CRUDTest(CRUDBase[TestStep, TestStepCreate, TestCaseUpdate]):
    pass


crud_test_step = CRUDTest(TestStep)

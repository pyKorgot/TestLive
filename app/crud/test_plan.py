from app.crud.base import CRUDBase
from app.models.test_plan import TestPlan
from app.schemas import TestPlanCreate, TestPlanUpdate


class CRUDTest(CRUDBase[TestPlan, TestPlanCreate, TestPlanUpdate]):
    pass


crud_test_plan = CRUDTest(TestPlan)

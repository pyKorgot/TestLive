from app.crud.base import CRUDBase
from app.models.test_plan import TestPlan
from app.schemas import TestPlanCreate, TestPlanUpdate


class CRUDTestPlan(CRUDBase[TestPlan, TestPlanCreate, TestPlanUpdate]):
    pass


crud_test_plan = CRUDTestPlan(TestPlan)

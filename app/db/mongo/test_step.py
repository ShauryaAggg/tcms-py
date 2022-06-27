from app.models.test_step import TestStep
from app.db.mongo.base import MongoBaseRepository


class TestStepRepository(MongoBaseRepository):
    class Meta:
        model = TestStep
        collection = "test_steps"

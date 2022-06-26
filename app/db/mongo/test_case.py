from app.models.test_case import TestCase
from app.db.mongo.base import MongoBaseRepository


class TestCaseRepository(MongoBaseRepository):
    class Meta:
        model = TestCase
        collection = "test_cases"

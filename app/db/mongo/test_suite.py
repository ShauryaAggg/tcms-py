from app.models.test_suite import TestSuite
from app.db.mongo.base import MongoBaseRepository


class TestSuiteRepository(MongoBaseRepository):
    class Meta:
        model = TestSuite
        collection = "test_suites"

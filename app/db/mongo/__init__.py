from app.db.mongo.mongo_store import MongoStore
from app.db.mongo.test_case import TestCaseRepository
from app.db.mongo.test_step import TestStepRepository
from app.db.mongo.test_suite import TestSuiteRepository
from app.db.mongo.user import UserRepository

repositories = {"test_case": TestCaseRepository,
                "test_step": TestStepRepository,
                "test_suite": TestSuiteRepository,
                "user": UserRepository}

store = MongoStore(
    "mongodb://mongoadmin:secret@localhost:27888/tcms?authSource=admin", repositories)

from app.db.mongo.mongo_store import MongoStore
from app.db.mongo.test_case import TestCaseRepository
from app.db.mongo.test_step import TestStepRepository

repositories = {"test_case": TestCaseRepository,
                "test_step": TestStepRepository}

store = MongoStore(
    "mongodb://mongoadmin:secret@localhost:27888/tcms?authSource=admin", repositories)

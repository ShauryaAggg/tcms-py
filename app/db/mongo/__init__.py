from app.db.mongo.mongo_store import MongoStore
from app.db.mongo.test_case import TestCaseRepository

repositories = {"test_case": TestCaseRepository}
store = MongoStore(
    "mongodb://mongoadmin:secret@localhost:27888/tcms?authSource=admin", repositories)

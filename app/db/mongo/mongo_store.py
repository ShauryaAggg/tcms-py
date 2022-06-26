from typing import Any, List, Mapping

import pymongo
from pymongo import database

from app.db.core.repository import Repository


class MongoStore:
    def __init__(self, db_uri: str, repositories: Mapping[str, "Repository"]) -> None:
        self._db_uri: str = db_uri
        self._db: database.Database = None
        self._client: pymongo.MongoClient = None
        self._repositories: Mapping[str, "Repository"] = {}

        self.connect()

        for key, repository in repositories.items():
            self._repositories[key] = repository(db=self._db)

    def connect(self) -> Any:
        client = pymongo.MongoClient(self._db_uri)
        self._db = client.get_database()
        self._client = client

    def disconnect(self):
        self._client.close()

    @property
    def database(self) -> Any:
        return self._db

    @property
    def repositories(self) -> Mapping[str, "Repository"]:
        return self._repositories

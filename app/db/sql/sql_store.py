from typing import Mapping, Any

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from app.db.core.repository import Repository


class SqlStore:
    """
    SQL Store for connecting to any SQL database.
    """

    def __init__(self, db_uri: str, repositories: Mapping[str, "Repository"]) -> None:
        """
        Initialize the store, connect to the database and initialize all repositories.

        :param db_uri: Database URI.
        :param repositories: Mapping of repository names to repository instances.
        """

        self._db_uri: str = db_uri
        self._db = None
        self._client: Engine = None
        self._repositories: Mapping[str, "Repository"] = {}

        self.connect()

        for key, repository in repositories.items():
            self._repositories[key] = repository(db=self._db)

    def connect(self) -> Any:
        engine = create_engine(self._db_uri)
        self._db = engine.connect()
        self._client = engine

    def disconnect(self):
        self._client.dispose()

    @property
    def database(self) -> Any:
        return self._db

    @property
    def repositories(self) -> Mapping[str, "Repository"]:
        return self._repositories

from typing import List

from app.models.base import Base
from app.models.test_case import TestCase
from app.models.core.index import IndexModel


class TestSuite(Base):
    """
    TestSuite model
    """

    name: str
    description: str
    test_cases: List["TestCase"]

    path: List[str]

    class Config:
        indexes = [
            IndexModel([("name", 1)]),
            IndexModel([("path", 1)]),
            IndexModel([("name", 1), ("path", 1)], unique=True)
        ]

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

    class Config:
        indexes = [
            IndexModel([("name", 1)])
        ]

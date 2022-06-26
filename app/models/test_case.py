from typing import List

from app.models.base import Base
from app.models.core.index import IndexModel


class TestCase(Base):
    name: str
    priority: int
    type: str
    steps: List[str]

    version: int
    last_edited_by: str

    class Config:
        indexes = [
            IndexModel(["version"], unique=True),
            IndexModel([("name", 1), ("priority", 1)])
        ]

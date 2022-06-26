from typing import List

from app.models.base import Base


class TestCase(Base):
    name: str
    priority: int
    type: str
    steps: List[str]

    version: int
    last_edited_by: str

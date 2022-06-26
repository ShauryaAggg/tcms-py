from pydoc import describe
from typing import List

from app.models.base import Base


class TestStep(Base):
    description: str
    parent: "TestStep"
    children: List["TestStep"]

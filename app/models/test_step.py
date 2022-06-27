from pydoc import describe
from typing import List, Optional

from app.models.base import Base


class TestStep(Base):
    description: str
    parent: Optional["TestStep"]
    children: Optional[List["TestStep"]]

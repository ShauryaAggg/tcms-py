from typing import List
from pydantic import BaseModel


class CreateTestCasePayload(BaseModel):
    name: str
    priority: int
    type: str
    steps: List[str]

    version: int
    last_edited_by: str

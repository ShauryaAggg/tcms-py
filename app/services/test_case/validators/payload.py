from typing import List, Optional
from pydantic import BaseModel


class CreateTestCasePayload(BaseModel):
    name: str
    priority: int
    type: str
    steps: List[str]

    version: int
    last_edited_by: str


class UpdateTestCasePayload(BaseModel):
    name: Optional[str]
    priority: Optional[int]
    type: Optional[str]
    steps: Optional[List[str]]

    version: Optional[int]
    last_edited_by: Optional[str]

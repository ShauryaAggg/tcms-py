from typing import List, Optional
from pydantic import BaseModel


class CreateTestStepPayload(BaseModel):
    description: str
    parent: Optional[str]
    children: Optional[List[str]]


class UpdateTestStepPayload(BaseModel):
    description: Optional[str]
    parent: Optional[str]
    children: Optional[List[str]]

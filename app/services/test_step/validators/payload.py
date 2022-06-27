from typing import List, Optional
from pydantic import BaseModel


class CreateTestStepPayload(BaseModel):
    description: str
    parent: Optional[str]
    children: Optional[List[str]]

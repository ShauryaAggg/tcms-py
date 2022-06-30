from typing import List, Optional
from pydantic import BaseModel


class CreateTestSuitePayload(BaseModel):
    name: str
    description: str
    test_cases: Optional[List[str]]


class UpdateTestSuitePayload(BaseModel):
    name: Optional[str]
    description: Optional[str]
    test_cases: Optional[List[str]]

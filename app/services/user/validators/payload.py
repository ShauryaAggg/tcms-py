from typing import Optional
from pydantic import BaseModel


class CreateUserPayload(BaseModel):
    name: str
    age: int
    email: str


class UpdateUserPayload(BaseModel):
    name: Optional[str]
    age: Optional[int]
    email: Optional[str]

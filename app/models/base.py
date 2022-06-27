import json
from typing import Any, Optional
from datetime import datetime
from bson import ObjectId

from pydantic import BaseModel, Field


class Base(BaseModel):
    """
    Base Model containing common fields
    """

    id: Any = Field(alias='_id')
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)

    class Config:
        json_encoders = {
            datetime: lambda x: x.isoformat(),
            ObjectId: lambda x: str(x)
        }

    def serialize(self):
        return json.loads(self.json())

from typing import Any, Optional
from datetime import datetime

from pydantic import BaseModel


class Base(BaseModel):
    id: Any
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

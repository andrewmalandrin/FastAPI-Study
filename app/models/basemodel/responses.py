from pydantic import BaseModel
from typing import Optional

class BasicResponseBase(BaseModel):
    status_code: int
    message: str
    error: Optional[bool] = False
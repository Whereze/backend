from typing import Optional
from pydantic.main import BaseModel

class Waterfall_model(BaseModel):
    uid: Optional[int]
    title: Optional[str]
    description: Optional[str]
    height: Optional[int]
    size: Optional[int]

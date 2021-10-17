from pydantic.main import BaseModel
from typing import Optional


class WaterfallModel(BaseModel):
    uid: Optional[int]
    title: str
    summary: str
    height: str
    width: str
    river: str
    country: str
    region: str
    RF_subject: str

    def __repr__(self) -> str:
        return f"WaterfallModel({self.uid}{self.title})"

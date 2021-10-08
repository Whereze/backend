from pydantic import BaseModel


class Waterfall(BaseModel):
    uid: int
    title: str
    description: str
    height: int
    size: int

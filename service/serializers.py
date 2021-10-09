from pydantic.main import BaseModel


class Waterfall(BaseModel):
    uid: int
    title: str
    description: str
    height: int
    size: int

    def __repr__(self) -> str:
        return f"Waterfall({self.uid}{self.title})"

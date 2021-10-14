from pydantic.main import BaseModel


class Waterfall(BaseModel):
    uid: int
    title: str
    summary: str
    url: str
    height: str
    width: str
    country: str
    region: str
    RF_subject: str

    def __repr__(self) -> str:
        return f"Waterfall({self.uid}{self.title})"

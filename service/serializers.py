from pydantic.main import BaseModel


class WaterfallModel(BaseModel):
    uid: int
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

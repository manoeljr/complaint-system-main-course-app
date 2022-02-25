from pydantic import BaseModel


class BaseComplaint(BaseModel):
    id: int
    title: str
    description: str
    photo_url: str
    amount: float

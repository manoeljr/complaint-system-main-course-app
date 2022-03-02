from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class BaseComplaint(BaseModel):
    id: int
    title: str
    description: str
    photo_url: str
    amount: float

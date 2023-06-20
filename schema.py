from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    date_of_birth: str
    place_of_birth: str

class User(UserCreate):
    id: int

    class Config:
        orm_mode = True

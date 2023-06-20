from sqlalchemy import Integer, Column, String

from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True,  index=True)
    name = Column(String)
    date_of_birth = Column(String)
    place_of_birth = Column(String)
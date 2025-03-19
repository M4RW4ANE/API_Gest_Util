from sqlmodel import Field, SQLModel, create_engine, String, Relationship
from typing import List
from user import Users

class Questions(SQLModel, table=True):
    id_question: int | None = Field(default=None, primary_key=True)
    question: str = Field(sa_column=String(200))
    
    users_id: List["Users"] = Relationship(back_populates="question")
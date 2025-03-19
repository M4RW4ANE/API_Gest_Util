
from sqlmodel import Field, SQLModel, create_engine, String, Relationship
from typing import List
from user import Users

class Role(SQLModel, table=True):
    __tablename__ ="roles" # Change le nom de la table
    id_Role: int | None = Field(default=None, primary_key=True)
    service: str = Field(sa_column=String(50))
    droit: str = Field(sa_column=String(50))
    
    users_id: List["Users"] = Relationship(back_populates="role")
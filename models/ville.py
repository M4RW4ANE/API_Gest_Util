from sqlmodel import Field, SQLModel, create_engine, String, Relationship
from typing import List
from rgpd import Rgpd

class Villes(SQLModel, table=True):
    id_ville: int | None = Field(default=None, primary_key=True)
    ville: str = Field(sa_column=String(50))
    code_postal: int = Field(max_digits=10)
    region: str = Field(sa_column=String(50))
    pays: str = Field(sa_column=String(50))
    
    rgpd_id: List["Rgpd"] = Relationship(back_populates="ville")
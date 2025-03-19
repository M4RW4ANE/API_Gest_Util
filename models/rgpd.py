from sqlmodel import Field, SQLModel, create_engine, String, Relationship
from datetime import date
from ville import Villes
from user import Users

class Rgpd(SQLModel, table=True):
    id_rgpd: int | None = Field(default=None, primary_key=True)
    nom : str = Field(sa_column=String(50))
    prenom: str = Field(sa_column=String(50))
    sex: str = Field(sa_column=String(50))
    date_de_naissance: date 
    mail: str = Field(sa_column=String(50))
    tel: int = Field(max_digits=25)
    
    ville_id: int = Field(default=None, foreign_key="villes.id_ville")
    ville: Villes = Relationship(back_populates="rgpd_id")
    
    user_id: int = Field(default=None, foreign_key="users.id_user")
    user: "Users" = Relationship(back_populates="rgpd")
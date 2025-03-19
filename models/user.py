from sqlmodel import Field, SQLModel, create_engine, String, Relationship
from role import Role
from question import Questions
from rgpd import Rgpd

class Users(SQLModel, table=True):
    id_user: int | None = Field(default=None, primary_key=True)
    password: str = Field(sa_column=String(50))
    reponse : str = Field(sa_column=String(50))
    
    role_id: int = Field(default=None, foreign_key="roles.id_Role")
    role: Role = Relationship(back_populates="users_id")

    question_id: int = Field(default=None, foreign_key="questions.id_question")
    question: Questions = Relationship(back_populates="users_id")

    rgpd_id: int = Field(default=None, foreign_key="rgpd.id_rgpd")
    rgpd: Rgpd = Relationship(back_populates="user_id")
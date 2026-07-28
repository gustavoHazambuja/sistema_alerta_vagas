from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True
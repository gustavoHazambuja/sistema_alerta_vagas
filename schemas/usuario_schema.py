from pydantic import BaseModel

class UsuarioCriar(BaseModel):
    nome: str
    email: str
    senha: str

class UsuarioResposta(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True
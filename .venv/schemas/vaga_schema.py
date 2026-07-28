from pydantic import BaseModel
from typing import Optional


class Vaga(BaseModel):
    id: int
    titulo: str
    localizacao: str
    modalidade: str
    salario_min: Optional[str] = None
    area: str

    class config:
        from_attributes = True


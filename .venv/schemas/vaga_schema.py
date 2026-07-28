from pydantic import BaseModel
from typing import Optional


class VagaCriar(BaseModel):
    titulo: str
    localizacao: str
    modalidade: str
    salario_min: Optional[float] = None
    area: str


class VagaResposta(VagaCriar):
      id: int

      class Config:
           from_attributes = True






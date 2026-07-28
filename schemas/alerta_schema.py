from pydantic import BaseModel
from typing import Optional


class AlertaCriar(BaseModel):
    palavra_chave: Optional[str] = None
    localizacao: Optional[str] = None
    modalidade: Optional[str] = None
    salario_min_desejado: Optional[str] = None


class AlertaResposta(AlertaCriar):
    id: int
    usuario_id: int
    ativo: bool


    class Config:
        from_attributes = True # Tradutor entre dicionários e objetos para o pydantic
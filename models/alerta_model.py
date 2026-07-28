from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from database import Base


class Alerta(Base):
    __tablename__ = "alertas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    palavra_chave = Column(String, nullable=True)
    localizacao = Column(String, nullable=True)
    modalidade = Column(String, nullable=True)
    salario_min_desejado = Column(Float, nullable=True)
    ativo = Column(Boolean, default=True)

from sqlalchemy import Column, Integer, String, Float
from database import Base


class Vaga(Base):
    __tablename__ = "vagas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    empresa = Column(String, nullable=False)
    localizacao = Column(String, nullable=False)
    modalidade = Column(String, nullable=False) # remoto, presencial, híbrido
    salario_min = Column(Float, nullable=True)
    area = Column(String, nullable=False)

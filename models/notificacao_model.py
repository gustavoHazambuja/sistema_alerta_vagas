from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime
from database import Base


class Notificacao(Base):
    __tablename__ = "notificacoes"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    vaga_id = Column(Integer, ForeignKey("vagas.id"), nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)
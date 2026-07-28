from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.vaga_model import Vaga
from models.alerta_model import Alerta
from schemas.vaga_schema import VagaCriar, VagaResposta
from services.alerta_service import processar_nova_vaga


router = APIRouter(prefix="/vagas", tags=["Vagas"])


@router.post("/criar", response_model=VagaResposta)
def criar_vaga(dados: VagaCriar, db: Session = Depends(get_db)):
    nova_vaga = Vaga(**dados.model_dump())
    db.add(nova_vaga)
    db.commit()
    db.refresh(nova_vaga)


    alertas_ativos = db.query(Alerta).filter(Alerta.ativo == True).all()
    processar_nova_vaga(db, nova_vaga, alertas_ativos)

    return nova_vaga


@router.get(response_model=list[VagaResposta])
def listar_vagas(db: Session = Depends(get_db)):
    return db.query(Vaga).all()



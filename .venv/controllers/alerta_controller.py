from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.alerta_model import Alerta
from schemas.alerta_schema import AlertaCriar, AlertaResposta


router = APIRouter(prefix="/alertas", tags=["Alertas"])


@router.post("/criar", response_model=AlertaResposta)
def criar_alerta(dados: AlertaCriar, usuario_id: int, db: Session = Depends(get_db)):
    novo_alerta = Alerta(usuario_id = usuario_id, **dados.model_dump())
    db.add(novo_alerta)
    db.commit()
    db.refresh(novo_alerta)
    return novo_alerta


@router.get("/{usuario_id}", response_model=AlertaResposta)
def listar_alertas_do_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return db.query(Alerta).filter(Alerta.usuario_id == usuario_id).all()


@router.patch("/{alerta_id}", response_model=AlertaResposta)
def pausar_alerta(alerta_id: int, db: Session = Depends(get_db)):

    alerta = db.query(Alerta).filter(Alerta.id == alerta_id).fist()
    if not alerta:
        raise HTTPException(status_code=404, detail= "Alerta não encontrado.")

    alerta.ativo = False
    db.commit()
    db.refresh(alerta)
    return alerta


@router.delete("/{alerta_id}", response_model=AlertaResposta)
def deletar_alerta(alerta_id: int, db: Session = Depends(get_db)):

    alerta = db.query(Alerta).filter(Alerta.id == alerta_id).fist()
    if not alerta:
        raise HTTPException(status_code=404, detail= "Alerta não encontrado.")

    db.delete(alerta)
    db.commit()
    
    return {"mensagem": "Alerta removido com sucesso."}


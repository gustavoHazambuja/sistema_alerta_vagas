from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.usuario_model import Usuario
from schemas.usuario_schema import UsuarioCriar, UsuarioResposta



router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("/criar", response_model=UsuarioResposta)
def criar_usuario(dados: UsuarioCriar, db: Session = Depends(get_db)):

    ja_existe = db.query(Usuario).filter(Usuario.email == dados.email).first()
    if ja_existe:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")


    novo_usuario = Usuario(
        nome = dados.nome,
        email = dados.email,
        senha = dados.senha
    )
    db.add(novo_usuario) # Salva na memória, não no banco
    db.commit() # Agora sim, salva no banco
    db.refresh(novo_usuario) # Gerando o id
    return novo_usuario


@router.get("/{usuario_id}", response_model=UsuarioResposta)
def buscar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")

    return usuario


@router.get("/", response_model=list[UsuarioResposta])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()
    
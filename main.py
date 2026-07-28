from fastapi import FastAPI

from database import Base, engine

from models import usuario_model, vaga_model, alerta_model, notificacao_model

from controllers import usuario_controller, vaga_controller, alerta_controller


app = FastAPI(
    title="Sistema de Alerta de Vagas",
    description="API que notifica usuários quando surgem vagas compatíveis com seus critérios",
    version="1.0.0"
)

# cria as tabelas no banco (se ainda não existirem) com base nos Models
Base.metadata.create_all(bind=engine)


# registra as rotas de cada controller na aplicação
app.include_router(usuario_controller.router)
app.include_router(vaga_controller.router)
app.include_router(alerta_controller.router)


@app.get("/")
def raiz():
    return {"mensagem": "API de Alerta de Vagas rodando"}
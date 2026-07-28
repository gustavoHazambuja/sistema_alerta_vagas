# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. String de conexão com o Postgres
# formato: postgresql://usuario:senha@host:porta/nome_do_banco
URL_BANCO = "postgresql://postgres:banco123@localhost:5432/vagas_db"

# 2. Engine: o "motor" que sabe conversar com o Postgres de fato
engine = create_engine(URL_BANCO)

# 3. Fábrica de sessões: cada chamada dela cria uma sessão nova
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base: classe da qual todos os seus Models (Usuario, Vaga, Alerta...) herdam
Base = declarative_base()


# 5. A dependency em si
def get_db():
    db = SessionLocal()   # abre uma sessão (o "carro" sai da garagem)
    try:
        yield db          # entrega o carro pro controller usar
    finally:
        db.close()        # não importa o que aconteceu, devolve o carro
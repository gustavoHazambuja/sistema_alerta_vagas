# Sistema de Alerta de Vagas
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/gustavohazambuja/sistema_alerta_vagas/blob/master/LICENSE)
 
# Sobre o projeto
Sistema de Alerta de Vagas é uma aplicação backend que consiste em uma API para gerenciamento de alertas de vagas de emprego, permitindo que usuários cadastrem critérios personalizados (palavra-chave, localização, modalidade e salário mínimo) e recebam notificações automáticas sempre que uma vaga compatível for publicada.
 
Nela podemos cadastrar usuários, criar e gerenciar alertas de busca, pausar ou remover alertas existentes, e cadastrar vagas que disparam automaticamente uma regra de negócio (matching) responsável por comparar a vaga com todos os alertas ativos e gerar notificações apenas para os que realmente combinam, evitando duplicidade de avisos para o mesmo usuário.
 
O projeto segue uma arquitetura em camadas (Models, Schemas, Controllers e Services), separando a representação dos dados, a validação de entrada/saída e as regras de negócio de matching.
 
# Tecnologias utilizadas
## Back end
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Uvicorn
# Como executar o projeto
Pré-requisitos: Python 3.11+ e PostgreSQL instalados.
 
## Executando localmente
 
1. Clone o repositório:
```
git clone https://github.com/gustavohazambuja/sistema_alerta_vagas.git
cd sistema_alerta_vagas
```
 
2. Crie e ative o ambiente virtual:
```
python -m venv .venv
source .venv/Scripts/activate
```
 
3. Instale as dependências:
```
pip install "fastapi[standard]" sqlalchemy psycopg2-binary
```
 
4. Crie o banco de dados no PostgreSQL:
```
psql -h localhost -U postgres -c "CREATE DATABASE vagas_db;"
```
 
5. Execute a aplicação (as tabelas são criadas automaticamente na primeira execução):
```
fastapi dev main.py
```
 
6. A aplicação estará disponível em:
```
http://localhost:8000
```
 
7. Documentação interativa (Swagger):
```
http://localhost:8000/docs
```
 
# Endpoints Principais:
- Usuários: POST /usuarios/criar
- Usuários: GET /usuarios/{usuario_id}
- Usuários: GET /usuários/
- Alertas: POST /alertas/criar/{usuario_id}
- Alertas: GET /alertas/{usuario_id}
- Alertas: PATCH /alertas/{alerta_id}/pausar
- Alertas: DELETE /alertas/{alerta_id}
- Vagas: POST /vagas/criar
- Vagas: GET /vagas/
# Autor
Gustavo Henrique Azambuja

https://www.linkedin.com/in/gustavohazambuja/

from fastapi import FastAPI

from app.database import Base, engine
from app.routers import atleta, categoria, centro_treinamento
from fastapi_pagination import add_pagination

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Workout API - Desafio DIO",
    description="""API de exemplo baseada no projeto da DIO.

Modificações implementadas para o desafio:
- Query parameters (nome, cpf) no endpoint GET /atletas
- Customização da response do GET /atletas
- Tratamento de sqlalchemy.exc.IntegrityError com status 303
- Paginação com limit e offset usando fastapi-pagination
""",
    version="1.0.0",
)

app.include_router(centro_treinamento.router)
app.include_router(categoria.router)
app.include_router(atleta.router)

# adiciona suporte global à paginação
add_pagination(app)

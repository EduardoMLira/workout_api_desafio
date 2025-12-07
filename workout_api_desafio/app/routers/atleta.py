from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import paginate
from fastapi_pagination.limit_offset import LimitOffsetPage

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/atletas", tags=["Atletas"])


@router.post("/", response_model=schemas.AtletaOut, status_code=status.HTTP_201_CREATED)
def criar_atleta(atleta_in: schemas.AtletaCreate, db: Session = Depends(get_db)):
    atleta = models.Atleta(**atleta_in.dict())
    try:
        db.add(atleta)
        db.commit()
        db.refresh(atleta)
        return atleta
    except IntegrityError:
        db.rollback()
        # requisito do desafio: manipular IntegrityError
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta_in.cpf}",
        )


@router.get(
    "/", response_model=LimitOffsetPage[schemas.AtletaListItem], status_code=status.HTTP_200_OK
)
def listar_atletas(
    nome: Optional[str] = None,
    cpf: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """Lista atletas com paginação por limit e offset.

    Requisitos implementados:
    - Query parameters: nome e cpf.
    - Paginação (fastapi-pagination) com limit e offset.
    - Response customizada exibindo apenas:
        - nome
        - centro_treinamento
        - categoria
    """
    query = (
        db.query(models.Atleta)
        .options(
            joinedload(models.Atleta.centro_treinamento),
            joinedload(models.Atleta.categoria),
        )
    )

    if nome:
        query = query.filter(models.Atleta.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(models.Atleta.cpf == cpf)

    atletas = query.order_by(models.Atleta.nome).all()

    items = [
        schemas.AtletaListItem(
            nome=a.nome,
            centro_treinamento=a.centro_treinamento.nome
            if a.centro_treinamento
            else "",
            categoria=a.categoria.nome if a.categoria else "",
        )
        for a in atletas
    ]

    return paginate(items)


@router.get(
    "/{atleta_id}",
    response_model=schemas.AtletaOut,
    status_code=status.HTTP_200_OK,
)
def buscar_atleta(atleta_id: int, db: Session = Depends(get_db)):
    atleta = (
        db.query(models.Atleta)
        .options(
            joinedload(models.Atleta.centro_treinamento),
            joinedload(models.Atleta.categoria),
        )
        .filter(models.Atleta.id == atleta_id)
        .first()
    )
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Atleta não encontrado."
        )
    return atleta

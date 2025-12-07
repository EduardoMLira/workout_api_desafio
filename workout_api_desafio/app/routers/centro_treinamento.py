from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/centros_treinamento", tags=["Centros de Treinamento"])


@router.post(
    "/", response_model=schemas.CentroTreinamentoOut, status_code=status.HTTP_201_CREATED
)
def criar_centro_treinamento(
    centro_in: schemas.CentroTreinamentoCreate, db: Session = Depends(get_db)
):
    centro = models.CentroTreinamento(**centro_in.dict())
    try:
        db.add(centro)
        db.commit()
        db.refresh(centro)
        return centro
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=f"Já existe um centro de treinamento cadastrado com o nome: {centro_in.nome}",
        )


@router.get("/", response_model=List[schemas.CentroTreinamentoOut])
def listar_centros_treinamento(db: Session = Depends(get_db)):
    return db.query(models.CentroTreinamento).all()

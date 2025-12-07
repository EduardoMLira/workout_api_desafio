from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.post("/", response_model=schemas.CategoriaOut, status_code=status.HTTP_201_CREATED)
def criar_categoria(
    categoria_in: schemas.CategoriaCreate, db: Session = Depends(get_db)
):
    categoria = models.Categoria(**categoria_in.dict())
    try:
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=f"Já existe uma categoria cadastrada com o nome: {categoria_in.nome}",
        )


@router.get("/", response_model=List[schemas.CategoriaOut])
def listar_categorias(db: Session = Depends(get_db)):
    return db.query(models.Categoria).all()

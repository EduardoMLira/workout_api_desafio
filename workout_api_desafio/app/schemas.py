from typing import Optional

from pydantic import BaseModel, Field


class CentroTreinamentoBase(BaseModel):
    nome: str = Field(..., example="CT DIO Sports")
    endereco: str = Field(..., example="Rua das APIs, 123 - São Paulo/SP")


class CentroTreinamentoCreate(CentroTreinamentoBase):
    pass


class CentroTreinamentoOut(CentroTreinamentoBase):
    id: int

    class Config:
        orm_mode = True


class CategoriaBase(BaseModel):
    nome: str = Field(..., example="Peso leve")


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaOut(CategoriaBase):
    id: int

    class Config:
        orm_mode = True


class AtletaBase(BaseModel):
    nome: str
    cpf: str
    idade: Optional[int] = None
    peso: Optional[float] = None
    altura: Optional[float] = None
    centro_treinamento_id: int
    categoria_id: int


class AtletaCreate(AtletaBase):
    pass


class AtletaOut(BaseModel):
    id: int
    nome: str
    cpf: str
    idade: Optional[int]
    peso: Optional[float]
    altura: Optional[float]
    centro_treinamento: CentroTreinamentoOut
    categoria: CategoriaOut

    class Config:
        orm_mode = True


class AtletaListItem(BaseModel):
    """Schema customizado para o endpoint GET ALL de atletas.

    Requisito do desafio: retornar apenas
    - nome
    - centro_treinamento
    - categoria
    """

    nome: str
    centro_treinamento: str
    categoria: str

    class Config:
        orm_mode = True

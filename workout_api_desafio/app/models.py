from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class CentroTreinamento(Base):
    __tablename__ = "centros_treinamento"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True, nullable=False)
    endereco = Column(String, nullable=False)

    atletas = relationship("Atleta", back_populates="centro_treinamento")


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True, nullable=False)

    atletas = relationship("Atleta", back_populates="categoria")


class Atleta(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True)
    cpf = Column(String, unique=True, nullable=False, index=True)
    idade = Column(Integer, nullable=True)
    peso = Column(Float, nullable=True)
    altura = Column(Float, nullable=True)

    centro_treinamento_id = Column(Integer, ForeignKey("centros_treinamento.id"))
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    centro_treinamento = relationship("CentroTreinamento", back_populates="atletas")
    categoria = relationship("Categoria", back_populates="atletas")

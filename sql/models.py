from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Obra(Base):
    __tablename__ = "obra"

    id_obra = Column(String(10), primary_key=True, index=True)
    nombre_obra = Column(String, index=True)


class Proyecto(Base):
    __tablename__ = "proyecto"

    id_proyecto = Column(String(10), primary_key=True, index=True)
    nombre_proyecto = Column(String, index=True)
    id_obra = Column(String(10), ForeignKey("obra.id_obra"))


class FrenteObra(Base):
    __tablename__ = "frenteobra"

    id_frenteObra = Column(String(10), primary_key=True, index=True)
    nombre_frenteObra = Column(String, index=True)
    id_proyecto = Column(String(10), ForeignKey("proyecto.id_proyecto"))


class Supervisora(Base):
    __tablename__ = "supervisora"

    id_supervisora = Column(String(10), primary_key=True, index=True)
    nombre_supervisora = Column(String, index=True)
    id_frenteObra = Column(String(10), ForeignKey("frenteobra.id_frenteObra"))


class Contratante(Base):
    __tablename__ = "contratante"

    id_contratante = Column(String(10), primary_key=True, index=True)
    nombre_contratante = Column(String, index=True)
    id_frenteObra = Column(String(10), ForeignKey("supervisora.id_frenteObra"))

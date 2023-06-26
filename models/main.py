from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sql.database import Base


class Obra(Base):
    __tablename__ = "obra"

    id_obra = Column(String(10), primary_key=True, index=True)
    nombre_obra = Column(String, index=True)


class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(String(10), primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, index=True)
    apellido = Column(String, index=True)
    password = Column(String, index=True)
    rol = Column(String, index=True)

    catalogs = relationship("Catalogo", back_populates="owner")


class Conceptos(Base):
    __tablename__ = "conceptos"

    clave = Column(String(10), primary_key=True, index=True)
    nombre = Column(String, index=True)
    unidad = Column(String, index=True)
    importe = Column(Float)
    precio = Column(Float)
    cantidad = Column(Integer)
    descripcion = Column(String)


class Catalogo(Base):
    __tablename__ = "catalogo_conceptos"

    id = Column(String, primary_key=True, index=True)
    id_superintendente = Column(String, ForeignKey("usuario.id_usuario"))
    nombre = Column(String, index=True)
    fecha = Column(Date, index=True)

    owner = relationship("Usuario", back_populates="catalogs")


class ConceptoEnCatalogo(Base):
    __tablename__ = "conceptos_en_catalogo"

    catalogo = Column(String, ForeignKey("catalogo_conceptos.id"))
    clave = Column(String, ForeignKey("conceptos.clave"))
    id = Column(Integer, primary_key=True, index=True)

    # catalogs = relationship("Catalogo", back_populates="catalogo_conceptos")
    # concepts = relationship("Conceptos", back_populates="conceptos")

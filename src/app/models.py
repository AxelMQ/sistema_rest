from sqlalchemy import Column, Integer, String
import uuid
from .db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    fecha_nac = Column(String, nullable=False)
    estado_civil = Column(String, nullable=False)
    transaccion_id = Column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)



    def to_dict(self):
        return {
            "id": self.id, 
            "nombre": self.nombre,
            "apellido": self.apellido,
            "direccion": self.direccion,
            "fecha_nac": self.fecha_nac,
            "estado_civil": self.estado_civil,
            "transaccion_id": self.transaccion_id
            }
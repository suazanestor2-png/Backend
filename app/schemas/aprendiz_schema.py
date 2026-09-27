from pydantic import BaseModel, ConfigDict
from typing import Optional


class AprendizBase(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    documento: Optional[str] = None
    tipo_documento: Optional[str] = None
    fecha_nacimiento: Optional[str] = None
    programa_formacion: Optional[str] = None
    ficha: Optional[str] = None


class AprendizCreate(AprendizBase):
    pass


class AprendizUpdate(AprendizBase):
    pass


class AprendizOut(AprendizBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
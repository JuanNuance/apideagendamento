from pydantic import BaseModel
from typing import Optional

class AparelhoBase(BaseModel):
    marca: str
    modelo: str
    numero_serie: str
    cliente_id: int

class AparelhoCreate(AparelhoBase):
    pass

class AparelhoUpdate(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    numero_serie: Optional[str] = None
    cliente_id: Optional[int] = None

class Aparelho(AparelhoBase):
    id: int
    
    class Config:
        from_attributes = True
        orm_mode = True
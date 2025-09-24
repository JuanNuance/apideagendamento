from pydantic import BaseModel, EmailStr
from typing import List, Optional

class ClientBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class Client(ClientBase):
    id: int
    
    class Config:
        from_attributes = True
        orm_mode = True
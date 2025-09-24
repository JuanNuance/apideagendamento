from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.connection import Base

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    address = Column(String, index=True)
    
    # Relacionamento com aparelhos
    aparelhos = relationship("Aparelho", back_populates="cliente")
    
    def __repr__(self):
        return f"<Client(id={self.id}, name='{self.name}', email='{self.email}')>"

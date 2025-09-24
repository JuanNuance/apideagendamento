from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Aparelho(Base):
    __tablename__ = "aparelhos"
    
    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String, index=True)
    numero_serie = Column(String, unique=True, index=True)
    
    # Foreign key corrigida
    cliente_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    
    # Relacionamento com cliente
    cliente = relationship("Client", back_populates="aparelhos")
    
    def __repr__(self):
        return f"<Aparelho(id={self.id}, marca='{self.marca}', modelo='{self.modelo}', numero_serie='{self.numero_serie}')>"

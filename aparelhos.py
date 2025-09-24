from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.connection import get_db
from models.aparelhos import Aparelho
from schemas.aparelhos import Aparelho as AparelhoSchema, AparelhoCreate, AparelhoUpdate

router = APIRouter(prefix="/aparelhos", tags=["Aparelhos"])

# CREATE
@router.post("/", response_model=AparelhoSchema)
def create_aparelho(aparelho: AparelhoCreate, db: Session = Depends(get_db)):
    db_aparelho = Aparelho(**aparelho.dict())
    db.add(db_aparelho)
    db.commit()
    db.refresh(db_aparelho)
    return db_aparelho

# READ
@router.get("/", response_model=List[AparelhoSchema])
def list_aparelhos(db: Session = Depends(get_db)):
    return db.query(Aparelho).all()

@router.get("/{aparelho_id}", response_model=AparelhoSchema)
def get_aparelho(aparelho_id: int, db: Session = Depends(get_db)):
    aparelho = db.query(Aparelho).filter(Aparelho.id == aparelho_id).first()
    if not aparelho:
        raise HTTPException(status_code=404, detail="Aparelho não encontrado")
    return aparelho

# UPDATE
@router.put("/{aparelho_id}", response_model=AparelhoSchema)
def update_aparelho(aparelho_id: int, updated_aparelho: AparelhoUpdate, db: Session = Depends(get_db)):
    aparelho = db.query(Aparelho).filter(Aparelho.id == aparelho_id).first()
    if not aparelho:
        raise HTTPException(status_code=404, detail="Aparelho não encontrado")
    
    # Atualizar apenas campos fornecidos
    update_data = updated_aparelho.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(aparelho, key, value)
    
    db.commit()
    db.refresh(aparelho)
    return aparelho

# DELETE
@router.delete("/{aparelho_id}")
def delete_aparelho(aparelho_id: int, db: Session = Depends(get_db)):
    aparelho = db.query(Aparelho).filter(Aparelho.id == aparelho_id).first()
    if not aparelho:
        raise HTTPException(status_code=404, detail="Aparelho não encontrado")
    
    db.delete(aparelho)
    db.commit()
    return {"detail": "Aparelho deletado com sucesso"}

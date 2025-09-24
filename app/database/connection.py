from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL corrigida (porta 5432)
DATABASE_URL = "postgresql://juanmonte@localhost:5432/minhaloja"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Função para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

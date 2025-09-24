from fastapi import FastAPI
from database.connection import Base, engine
from routers import clients, aparelhos

# Criar tabelas no banco
Base.metadata.create_all(bind=engine)

# Inicializar aplicação
app = FastAPI(
    title="Sistema de Gestão",
    description="API para gestão de clientes e aparelhos",
    version="1.0.0"
)

# Incluir rotas
app.include_router(clients.router)
app.include_router(aparelhos.router)

@app.get("/")
def read_root():
    return {"message": "API Sistema de Gestão"}

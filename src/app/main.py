import uvicorn
from fastapi import FastAPI, status
from typing import Dict
from app.routers.api import router as ai_router

# 1. Instanciação da API FastAPI com metadados executivos
app = FastAPI(
    title="Skill2Income AI Engines",
    description="Engine de Inteligência Artificial para descoberta, mapeamento e monetização de competências profissionais.",
    version="1.0.0"
)

# 2. Inclusão dos Roteadores Oficiais (Movido para após a criação da instância 'app')
# Este roteador ativa o endpoint POST /api/v1/analyze integrado aos motores reais de IA.
app.include_router(ai_router)


# 3. Endpoint de Monitoramento (Health Check)
@app.get("/health", status_code=status.HTTP_200_OK, tags=["Health Check"])
def health_check() -> Dict[str, str]:
    """
    Retorna o status de saúde da aplicação e dos motores de IA.
    Utilizado por orquestradores (Docker/Render) para checar a integridade do container.
    """
    return {"status": "healthy", "engine_status": "operational"}


# 4. Bloco de Inicialização de Desenvolvimento Local
if __name__ == "__main__":
    # Ajustado para 'app.main:app' garantindo compatibilidade com o PYTHONPATH da raiz do projeto
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

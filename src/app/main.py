import uvicorn
from fastapi import FastAPI, HTTPException, status
from app.models.recommendation import Skill2IncomeResponse
from typing import Dict
from app.routers.api import router as ai_router
app.include_router(ai_router)



app = FastAPI(
    title="Skill2Income AI Engines",
    description="Engine de Inteligência Artificial para descoberta, mapeamento e monetização de competências profissionais.",
    version="1.0.0"
)

@app.get("/health", status_code=status.HTTP_200_OK, tags=["Health Check"])
def health_check() -> Dict[str, str]:
    """Retorna o status de saúde da aplicação e dos motores de IA."""
    return {"status": "healthy", "engine_status": "operational"}

@app.post("/api/v1/analyze", response_model=Skill2IncomeResponse, status_code=status.HTTP_200_OK, tags=["AI Core Engine"])
async def analyze_skills(user_profile: Dict[str, str]):
    """
    Consome o payload do usuário (Currículo/Respostas do Mapa)
    e invoca as camadas do SkillExtractor e MonetizationEngine.
    """
    if not user_profile.get("raw_text"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="O campo 'raw_text' com as informações profissionais é obrigatório para análise."
        )
    
    try:
        # Aqui o ecossistema invocará os serviços do src/app/services/ai/
        # Simulação de resposta estruturada conforme contrato Pydantic para fins de arquitetura
        mock_response = {
            "usuario_id": "usr_santos_2026",
            "skills_identificadas": {
                "tecnicas": ["Python", "SQL", "FastAPI", "Power BI", "Docker", "Machine Learning"],
                "comportamentais": ["Liderança Técnica", "Mitigação de Risco", "Tomada de Decisão"],
                "criativas": ["Storytelling de Dados", "Produção de Conteúdo Técnico"]
            },
            "plano_monetizacao": [
                {
                    "servico": "Desenvolvimento de Dashboards Inteligentes de Risco",
                    "plataforma_sugerida": "LinkedIn / Contratos Diretos B2B",
                    "ticket_medio_reais": 1500.00,
                    "justificativa_negocio": "Pequenas empresas e operações de logística sofrem com atrasos e necessitam de visibilidade preditiva de perdas."
                },
                {
                    "servico": "Automação de Pipelines de Dados e Scripts de RPA",
                    "plataforma_sugerida": "Workana / Fiverr",
                    "ticket_medio_reais": 2000.00,
                    "justificativa_negocio": "Substituição de processos manuais repetitivos por rotinas automatizadas robustas em Python para redução de horas de trabalho de staff."
                }
            ],
            "potencial_renda_mensal_estimado": 3500.00
        }
        return mock_response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Falha crítica na execução das inferências dos motores de IA: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

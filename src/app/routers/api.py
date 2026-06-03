from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from app.models.recommendation import Skill2IncomeResponse
from app.services.ai.skill_extractor import SkillExtractor
from app.services.ai.monetization_engine import MonetizationEngine

router = APIRouter(prefix="/api/v1", tags=["AI Core Pipeline"])

class AnalysisRequest(BaseModel):
    usuario_id: str = Field(..., example="usr_santos_2026")
    raw_text: str = Field(..., description="Texto do currículo ou respostas do inventário da DIO")

@router.post("/analyze", response_model=Skill2IncomeResponse, status_code=status.HTTP_200_OK)
async def process_skill_to_income_pipeline(payload: AnalysisRequest):
    """
    Pipeline completa de IA End-to-End:
    1. Ingestão de dados não estruturados.
    2. Extração estruturada de Skills (Diretrizes DIO).
    3. Mapeamento de demanda econômica e cálculo de potencial de renda (Métricas Meigarom).
    """
    try:
        # Instanciação dos motores inteligentes de IA
        extractor = SkillExtractor()
        monetizer = MonetizationEngine()
        
        # Passo 1: Executa a extração assíncrona das competências do usuário
        skills_extracted = await extractor.extract(payload.raw_text)
        
        # Passo 2: Alimenta o motor de monetização com as skills validadas
        monetization_plan = await monetizer.generate_plan(skills_extracted)
        
        # Passo 3: Calcula a métrica de Business Performance (Potencial Financeiro Acumulado)
        potencial_total = sum(item.ticket_medio_reais for item in monetization_plan)
        
        # Retorna o contrato perfeito exigido pelo cliente
        return Skill2IncomeResponse(
            usuario_id=payload.usuario_id,
            skills_identificadas=skills_extracted,
            plano_monetizacao=monetization_plan,
            potencial_renda_mensal_estimado=potencial_total
        )
        
    except RuntimeError as r_err:
        # Tratamento de erro direcionado a falhas nos serviços de IA externos
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(r_err)
        )
    except Exception as e:
        # Proteção global contra falhas não mapeadas
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro interno de processamento na pipeline principal: {str(e)}"
        )

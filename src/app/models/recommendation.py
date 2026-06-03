from pydantic import BaseModel, Field
from typing import List, Dict

class SkillClassification(BaseModel):
    tecnicas: List[str] = Field(..., description="Habilidades de ferramentas, linguagens e frameworks")
    comportamentais: List[str] = Field(..., description="Habilidades de liderança, comunicação e postura")
    criativas: List[str] = Field(..., description="Habilidades de geração de conteúdo, design ou inovação")

class MonetizationOpportunity(BaseModel):
    servico: str = Field(..., description="Nome do produto ou serviço a ser vendido")
    plataforma_sugerida: str = Field(..., description="Onde anunciar o serviço (Ex: Fiverr, Workana)")
    ticket_medio_reais: float = Field(..., description="Valor estimado de cobrança baseado em mercado")
    justificativa_negocio: str = Field(..., description="O porquê existe demanda real para isso")

class Skill2IncomeResponse(BaseModel):
    usuario_id: str
    skills_identificadas: SkillClassification
    plano_monetizacao: List[MonetizationOpportunity]
    potencial_renda_mensal_estimado: float

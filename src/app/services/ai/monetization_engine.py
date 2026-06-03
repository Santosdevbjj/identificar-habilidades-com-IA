import os
import httpx
from typing import List
from openai import AsyncOpenAI
from pydantic import BaseModel, Field
from app.models.recommendation import SkillClassification, MonetizationOpportunity

# Auxiliar para tipagem da lista no Structured Output da OpenAI
class MonetizationPlanWrapper(BaseModel):
    oportunidades: List[MonetizationOpportunity] = Field(..., description="Lista de caminhos de monetização validados")

class MonetizationEngine:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.prompt_path = os.path.join(
            os.path.dirname(__file__), "..", "prompts", "monetization.txt"
        )

    def _load_system_prompt(self) -> str:
        with open(self.prompt_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    async def generate_plan(self, skills: SkillClassification) -> List[MonetizationOpportunity]:
        """
        Consome o objeto estruturado de skills e gera o plano econômico de conversão em renda.
        """
        system_prompt = self._load_system_prompt()
        
        # Converte as listas estruturadas em payload textual limpo para a LLM
        user_payload = (
            f"Habilidades Técnicas: {', '.join(skills.tecnicas)}\n"
            f"Habilidades Comportamentais: {', '.join(skills.comportamentais)}\n"
            f"Habilidades Criativas: {', '.join(skills.criativas)}"
        )
        
        try:
            response = await self.client.beta.chat.completions.parse(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Gere oportunidades com base nesta matriz de competências:\n\n{user_payload}"}
                ],
                response_format=MonetizationPlanWrapper,
                temperature=0.3 # Ligeiramente maior para incentivar insights acionáveis criativos, sem perder o contrato JSON
            )
            
            parsed_result = response.choices[0].message.parsed
            if not parsed_result or not parsed_result.oportunidades:
                return []
                
            return parsed_result.oportunidades

        except httpx.HTTPStatusError as http_err:
            raise RuntimeError(f"Falha de comunicação com o provedor de precificação: {http_err}")
        except Exception as e:
            raise RuntimeError(f"Erro crítico no serviço MonetizationEngine: {str(e)}")

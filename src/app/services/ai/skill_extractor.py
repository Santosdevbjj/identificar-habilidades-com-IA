import os
import httpx
from openai import AsyncOpenAI
from app.models.recommendation import SkillClassification

class SkillExtractor:
    def __init__(self):
        # Utiliza cliente assíncrono preparado para alta concorrência (Padrão FAANG)
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.prompt_path = os.path.join(
            os.path.dirname(__file__), "..", "prompts", "skill_inventory.txt"
        )
        
    def _load_system_prompt(self) -> str:
        with open(self.prompt_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    async def extract(self, raw_text: str) -> SkillClassification:
        """
        Analisa o texto bruto do usuário e força um output estruturado 
        conforme o modelo Pydantic SkillClassification.
        """
        system_prompt = self._load_system_prompt()
        
        try:
            response = await self.client.beta.chat.completions.parse(
                model="gpt-4o-mini", # Modelo otimizado para Structured Outputs com latência ultrabaixa
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Analise o seguinte perfil profissional para extração:\n\n{raw_text}"}
                ],
                response_format=SkillClassification,
                temperature=0.1 # Baixa variabilidade para garantir consistência analítica
            )
            
            # O SDK analisa e valida automaticamente o JSON contra o modelo Pydantic
            validated_skills = response.choices[0].message.parsed
            if not validated_skills:
                raise ValueError("A IA retornou um formato nulo ou inválido.")
                
            return validated_skills

        except httpx.HTTPStatusError as http_err:
            # Tratamento de erro de infraestrutura de rede/API
            raise RuntimeError(f"Falha de comunicação com o provedor de IA: {http_err}")
        except Exception as e:
            # Fallback seguro para produção
            raise RuntimeError(f"Erro crítico no serviço SkillExtractor: {str(e)}")

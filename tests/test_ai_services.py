import pytest
from unittest.mock import AsyncMock, patch
from app.services.ai.skill_extractor import SkillExtractor
from app.services.ai.monetization_engine import MonetizationEngine
from app.models.recommendation import SkillClassification, MonetizationOpportunity

@pytest.mark.asyncio
@patch("app.services.ai.skill_extractor.AsyncOpenAI")
async def test_skill_extractor_success(mock_openai_class):
    """Garante que o SkillExtractor analisa o texto e retorna o objeto Pydantic esperado."""
    # Configuração do Mock para o Structured Output da OpenAI
    mock_client = AsyncMock()
    mock_openai_class.return_location = mock_client
    
    mock_parsed_response = SkillClassification(
        tecnicas=["Python", "SQL"],
        comportamentais=["Liderança Técnica"],
        criativas=["Storytelling de Dados"]
    )
    
    # Simula a estrutura interna de retorno do SDK da OpenAI (choices[0].message.parsed)
    mock_choice = AsyncMock()
    mock_choice.message.parsed = mock_parsed_response
    mock_client.beta.chat.completions.parse.return_value = AsyncMock(choices=[mock_choice])
    
    # Execução do teste com injeção do mock de arquivo
    with patch("builtins.open", patch.object):
        extractor = SkillExtractor()
        extractor.client = mock_client
        resultado = await extractor.extract("Texto profissional de teste de engenharia.")
        
        # Asserções de Validação
        assert resultado.tecnicas == ["Python", "SQL"]
        assert resultado.comportamentais == ["Liderança Técnica"]
        assert "Storytelling de Dados" in resultado.criativas
        mock_client.beta.chat.completions.parse.assert_called_once()

@pytest.mark.asyncio
@patch("app.services.ai.monetization_engine.AsyncOpenAI")
async def test_monetization_engine_empty_skills(mock_openai_class):
    """Valida se o motor de monetização lida corretamente com estruturas de skills vazias."""
    mock_client = AsyncMock()
    mock_openai_class.return_value = mock_client
    
    # Configura um retorno vazio simulado da LLM
    mock_choice = AsyncMock()
    mock_choice.message.parsed = AsyncMock(oportunidades=[])
    mock_client.beta.chat.completions.parse.return_value = AsyncMock(choices=[mock_choice])
    
    with patch("builtins.open", patch.object):
        engine = MonetizationEngine()
        engine.client = mock_client
        
        skills_vazias = SkillClassification(tecnicas=[], comportamentais=[], criativas=[])
        plano = await engine.generate_plan(skills_vazias)
        
        assert isinstance(plano, list)
        assert len(plano) == 0

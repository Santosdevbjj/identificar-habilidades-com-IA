import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from app.main import app

client = TestClient(app)

def test_health_check_endpoint():
    """Garante que a rota de monitoramento de saúde do sistema responde com sucesso (200 OK)."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "engine_status": "operational"}

def test_analyze_endpoint_bad_request():
    """Valida se a API rejeita corretamente requisições com payloads ausentes ou incompletos (422/400)."""
    # Payload sem o campo obrigatório 'raw_text'
    payload_invalido = {"usuario_id": "usr_santos_2026"}
    response = client.post("/api/v1/analyze", json=payload_invalido)
    
    # O Pydantic integrado ao FastAPI deve retornar erro de validação automaticamente
    assert response.status_code == 422

@patch("app.routers.api.SkillExtractor.extract")
@patch("app.routers.api.MonetizationEngine.generate_plan")
def test_analyze_pipeline_success_integration(mock_generate_plan, mock_extract):
    """Testa a integração fim a fim da pipeline simulando o processamento completo de uma requisição com sucesso."""
    
    # Configuração dos retornos fictícios dos objetos internos da pipeline de dados
    from app.models.recommendation import SkillClassification, MonetizationOpportunity
    
    mock_extract.return_value = SkillClassification(
        tecnicas=["Python", "Power BI"],
        comportamentais=["Organização"],
        criativas=["Aulas"]
    )
    
    mock_generate_plan.return_value = [
        MonetizationOpportunity(
            servico="Construção de Dashboards",
            plataforma_sugerida="Fiverr",
            ticket_medio_reais=500.00,
            justificativa_negocio="Empresas precisam de indicadores consolidados."
        )
    ]
    
    # Dispara a requisição HTTP POST contra a API local
    payload_valido = {
        "usuario_id": "usr_santos_2026",
        "raw_text": "Cientista de dados focado em risco com domínio em Python e Power BI."
    }
    response = client.post("/api/v1/analyze", json=payload_valido)
    data = response.json()
    
    # Validações estritas do contrato de resposta (Skill2IncomeResponse)
    assert response.status_code == 200
    assert data["usuario_id"] == "usr_santos_2026"
    assert "Python" in data["skills_identificadas"]["tecnicas"]
    assert data["potencial_renda_mensal_estimado"] == 500.00
    assert len(data["plano_monetizacao"]) == 1
    assert data["plano_monetizacao"][0]["plataforma_sugerida"] == "Fiverr"

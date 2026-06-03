# 4. Coleta dos Dados (Data Collection)

## Fontes de Ingestão do Sistema
O ecossistema **Skill2Income AI** foi projetado para atuar de forma agnóstica na camada de ingestão, processando fluxos de texto não estruturado de três fontes principais[span_0](start_span)[span_0](end_span):
1. **Currículo Profissional (CV):** Arquivos convertidos para texto contendo histórico de cargos, atribuições e projetos práticos[span_1](start_span)[span_1](end_span).
2. **Respostas do Inventário de Competências (Mapeamento DIO):** Respostas diretas às perguntas estruturadas de autoavaliação.
3. **Metadados de Perfil Corporativo:** Textos extraídos de seções como "Sobre" e "Experiência" do LinkedIn[span_2](start_span)[span_2](end_span).

## Estrutura do Payload de Entrada (Ingestão da API)
Os dados brutos entram no sistema via requisição HTTP POST sob um contrato estrito validado pelo FastAPI. Veja o esquema de dados do payload de entrada:

```json
{
  "usuario_id": "usr_santos_2026",
  "raw_text": "SÉRGIO LUIZ DOS SANTOS. Cientista de Dados focado na construção de produtos analíticos voltados à redução de risco e geração de impacto financeiro... Python | SQL | C# | .NET | Azure Databricks | Power BI | Docker[span_3](start_span)[span_3](end_span)."
}

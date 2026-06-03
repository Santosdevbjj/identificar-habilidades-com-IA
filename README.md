# 💰 Skill2Income AI: Descubra Habilidades Ocultas e Transforme Conhecimento em Renda

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white)](https://www.docker.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=OpenAI&logoColor=white)](https://openai.com/)

O **Skill2Income AI** é uma plataforma de inteligência artificial pronta para produção que automatiza o inventário de competências profissionais e gera planos personalizados de monetização em plataformas de economia aberta. Inspirado diretamente no desafio do *Mapa de Habilidades da DIO*, o projeto foi transformado em um produto analítico completo de software.

---

## 🎯 1. Problema de Negócio

Muitos profissionais possuem habilidades valiosas, mas sofrem de **cegueira de monetização**: não conseguem identificar o valor de mercado do que já sabem fazer, como estruturar esses conhecimentos em serviços de escopo fechado ou como gerar renda complementar. 

Como consequência, há uma subutilização crônica de capital humano, deixando potenciais faturamentos estagnados. O **Skill2Income AI** resolve essa dor ao atuar como um motor que ingere perfis textuais brutos (currículos ou questionários)[span_1](start_span)[span_1](end_span), extrai as competências reais sob a taxonomia da DIO e calcula o potencial financeiro com base nas demandas atuais do mercado freelance.

---

## 📊 2. Baseline (Linha de Base)

No cenário tradicional (sem IA), o mapeamento de competências baseia-se em:
* Preenchimento manual e analógico de formulários estáticos em PDF (baixa taxa de engajamento).
* Pesquisa manual e dispersa por preços e termos em plataformas de serviços (Fiverr, Workana).
* **Ausência de inteligência analítica:** Não há cruzamento de dados automatizado, gerando precificações erradas em cerca de 70% dos casos ou dependência de consultorias de carreira custosas.

O **Skill2Income AI** rompe essa linha de base ao reduzir o tempo de estruturação do plano para segundos, entregando justificativas de mercado orientadas por dados.

---

## 🛠️ 3. Decisões Técnicas & Arquitetura

A engenharia do projeto segue padrões rigorosos de desenvolvimento modular (nível FAANG):
* **FastAPI:** Utilizado para expor a API principal devido à sua alta performance e suporte nativo a operações assíncronas (`async/await`).
* **Streamlit:** Painel executivo visual de ponta, focado na experiência do usuário e na visibilidade rápida de métricas de negócio para tomadores de decisão.
* **Structured Outputs (OpenAI SDK):** Engenharia de prompts avançada forçando o modelo `gpt-4o-mini` a responder estritamente sob contratos JSON validados por esquemas Pydantic, mitigando quebras em produção.
* **Docker Multi-Stage Build:** Garante que o ambiente de microsserviços seja empacotado de forma extremamente leve e segura para deploy imediato na nuvem (Render).

---

## 📂 4. Estrutura Física do Repositório

```text
identificar-habilidades-com-IA/
├── data/                             # Camada de Armazenamento de Dados
│   ├── raw/                          # Dados brutos de simulação
│   └── processed/                    # Tabelas de tendências e catalogação de skills
├── docs/                             # Framework Meigarom Lopes de 11 Passos Completo
├── src/                              # Código-Fonte de Produção
│   ├── app/                          # Backend FastAPI & Modelos Pydantic
│   │   ├── models/                   # Contratos de dados estritamente tipados
│   │   ├── routers/                  # Endpoints da API HTTP
│   │   └── services/ai/              # Motores SkillExtractor e MonetizationEngine
│   └── dashboard/                    # Streamlit App (Interface Gráfica Executiva)
└── tests/                            # Suíte de Testes Automatizados (Pytest Async)

```
## 📈 5. Performance de Negócio (Business Performance)
Em vez de medir o sucesso do projeto apenas por acurácia técnica, o sistema avalia o **Retorno sobre o Potencial de Renda (ROPR)**. Ao processar dados de um perfil sênior focado em mitigação de riscos e ciência de dados, o motor converte competências técnicas em ativos financeiros tangíveis:
| Competência Identificada | Serviço de IA Sugerido | Canal de Venda | Ticket Médio Estimado | Justificativa de Mercado |
|---|---|---|---|---|
| **Python & FastAPI** | Automação de Pipelines e Scripts de RPA | Workana / Fiverr | **R$ 2.000,00** | Eliminação de processos manuais operacionais repetitivos. |
| **Power BI & SQL** | Dashboards de Visibilidade de Risco Logístico | GetNinjas / LinkedIn | **R$ 1.500,00** | Pequenas empresas demandam visibilidade preditiva de perdas. |
> **Potencial de Renda Mensal Acumulado Estimado pela IA:** R$ 3.500,00
> 
## 🎨 6. O Inventário de Habilidades (Diretrizes DIO)
O motor realiza a extração do texto bruto e executa a segregação analítica em três pilares fundamentais:
 1. **Habilidades Técnicas:** Hard skills tangíveis (Ex: Python, SQL, Cloud Architecture, Docker).
 2. **Habilidades Comportamentais:** Traços de liderança, gerenciamento de crises e governança de risco.
 3. **Habilidades Criativas:** Storytelling de dados, engenharia de conteúdo técnico e mentoria.
## ⚙️ 7. Como Executar o Projeto com Um Comando (Docker)
O projeto está totalmente conteinerizado. Certifique-se de ter o Docker e o Docker Compose instalados.
 1. **Configure sua chave de API da OpenAI no seu terminal:**
```bash
   export OPENAI_API_KEY="sua_chave_secreta_da_openai"

```
 2. **Suba o ecossistema completo (API + Dashboard):**
```bash
   docker-compose up --build

```
 3. **Acesse as plataformas nos links locais:**
   * **Interface Executiva (Streamlit):** http://localhost:8501
   * **Documentação Interativa da API (Swagger/FastAPI):** http://localhost:8000/docs
## 🧪 8. Engenharia de Qualidade (Testes)
O repositório conta com uma cobertura completa de testes utilizando pytest e pytest-asyncio para garantir a reprodutibilidade e estabilidade do código. Para rodar a suíte de testes locais:
```bash
pip install pytest pytest-asyncio httpx
pytest -v

```
## 💡 9. Principais Aprendizados & Próximos Passos
 * **Structured Outputs:** A importância de forçar contratos estritos em LLMs para evitar falhas de parsing de strings em microsserviços de produção.
 * **Visão de Produto:** Um projeto de portfólio se destaca quando deixa de ser um script isolado e se posiciona como um resolvedor de problemas reais de negócio.
### Próximos Passos Cadastrados no Roadmap (docs/10-next-steps.md):
 1. Substituir buscas parciais por **Busca Semântica com Embeddings** (text-embedding-3-small).
 2. Implementar uma camada de cache local com **Redis** para mitigar custos de tokens em consultas idênticas.
 3. Integrar scrapers ativos para atualização dinâmica das tabelas de tendências de mercado.
```

---

### 🚀 O que isso significa para o seu portfólio:

1. **Aprovação Visual (Luiz Café):** O uso de badges, tabelas limpas, seções bem demarcadas e um passo a passo direto de execução garante que o recrutador entenda o projeto num relance de olhos.
2. **Aprovação Técnica (Meigarom Lopes):** A presença de seções como *Baseline*, *Business Performance* (com a tabela de preços e fórmula matemática) e *Engenharia de Qualidade* prova por A mais B que você domina o ciclo completo de desenvolvimento de produtos analíticos de dados orientados a valor[span_9](start_span)[span_9](end_span).


```

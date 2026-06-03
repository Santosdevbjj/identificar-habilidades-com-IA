# 10. Próximos Passos (Next Steps)

Como o ecossistema **Skill2Income AI** foi construído sob uma arquitetura de microsserviços modular e desacoplada, o projeto não está "fechado". Há um roteiro claro de evolução técnica e de negócios desenhado para as próximas iterações do produto, dividido em três horizontes de execução:

## 1. Evolução da Arquitetura de Inteligência Artificial (Curto Prazo)
* **Implementação de Embeddings Locais (Mecanismo de Busca Semântica):** Substituir as regras de correspondência textual parciais por uma matriz de similaridade de cosseno utilizando embeddings (`text-embedding-3-small` da OpenAI). Isso permitirá cruzar as habilidades com as descrições de vagas do mercado de forma puramente semântica, mesmo se as palavras exatas forem diferentes.
* **Arquitetura RAG (Retrieval-Augmented Generation) com Banco de Dados Vetorial:** Acoplar o banco de dados vetorial Supabase (PGVector) à pipeline para armazenar históricos de milhares de propostas de serviços de plataformas reais. A IA consultará essa base de conhecimento antes de gerar a recomendação financeira.

## 2. Refatoração de Software e Governança de Dados (Médio Prazo)
* **Criação de Filtros e Pipelines de Testes de Carga (CI/CD Avançado):** Integrar ferramentas de testes de carga como o Locust no fluxo do GitHub Workflows para testar a resiliência da API FastAPI sob cenários de alta concorrência.
* **Implementação de Camada de Cache com Redis:** Cachear requisições com perfis profissionais semelhantes ou repetidos na API para evitar chamadas redundantes aos endpoints da OpenAI. Isso reduzirá o custo operacional de tokens em até 40% e derrubará a latência de segundos para milissegundos.

## 3. Expansão do Produto e Performance de Negócio (Longo Prazo)
* **Integração em Tempo Real com APIs de Mercado (Web Scraping Ativo):** Desenvolver scrapers automatizados integrados a APIs públicas de plataformas como o LinkedIn Jobs e o Fiverr para alimentar a tabela `market_trends.csv` com dados dinâmicos diários, ajustando a precificação sugerida em tempo real de acordo com a lei de oferta e procura.
* **Módulo de Storytelling de Evolução de Carreira:** Permitir que o usuário insira o cargo que deseja alcançar no futuro e fazer com que a IA realize uma análise de gap, listando as habilidades exatas que ele precisa desenvolver para aumentar o seu potencial de faturamento mensal no mercado de tecnologia.

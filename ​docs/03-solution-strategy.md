# 3. Estratégia de Solução

Para construir uma arquitetura limpa de nível FAANG, o fluxo de dados foi dividido em serviços desacoplados e tipados em Python[span_4](start_span)[span_4](end_span):

```
[Entrada de Dados Brutos] -> (FastAPI Validation) -> [Serviço Extrator de Habilidades]
│
(Categorização DIO)
│
▼
[Recomendação Econômica] <- (Motor de Precificação) <- [Mapeador de Demanda de Mercado]

```



## Divisão dos Componentes de IA
1. **`SkillExtractor` (Camada de Ingestão & NLP):** Consome dados não estruturados do usuário e do currículo[span_5](start_span)[span_5](end_span), aplicando engenharia de prompts estruturada para extrair e catalogar habilidades em três vertentes: Técnicas, Comportamentais e Criativas.
2. **`MarketMapper` (Camada de Negócio):** Realiza o enriquecimento dos dados simulando buscas analíticas por dores de mercado que correspondam àquelas competências.
3. **`MonetizationEngine` (Camada Financeira):** Converte a acurácia estatística das recomendações em matrizes de retorno financeiro e sugere canais de distribuição (Fiverr, GetNinjas, etc.).
4. 

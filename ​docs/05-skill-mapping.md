
#### 📄 `docs/05-skill-mapping.md`
```markdown
# 5. Mapeamento de Competências (Skill Mapping & EDA)

## Hipóteses de Negócio Validadas (Mapeamento Baseado no Framework)
Durante a estruturação do motor de IA, foram validadas três hipóteses centrais sobre perfis técnicos maduros:
* **Hipótese 1:** Profissionais seniores de infraestrutura e engenharia de software possuem habilidades comportamentais de alta resiliência (mitigação de riscos) que são mais valorizadas pelo mercado de consultoria do que o domínio de sintaxe pura de ferramentas[span_4](start_span)[span_4](end_span).
* **Hipótese 2:** A habilidade criativa de traduzir métricas estatísticas abstratas (MAE, RMSE) em tabelas de impacto financeiro (R$) constitui uma competência rara de Storytelling de Dados que destrava contratos de alto ticket[span_5](start_span)[span_5](end_span).
* **Hipótese 3:** Habilidades tradicionais como administração de servidores legados e governança de dados podem ser reempacotadas como serviços modernos de Consultoria de Continuidade de Negócios para PMEs[span_6](start_span)[span_6](end_span).

## Regras de Agrupamento Estruturado (Diretrizes DIO)
A IA realiza a categorização das palavras-chave normalizadas em três vetores ortogonais:



---

```


┌───────────────────────────────┐
│      SKILL CLASSIFICATION     │
└───────────────┬───────────────┘
┌───────────────────────┼───────────────────────┐
▼                       ▼                       ▼
┌───────────────────┐   ┌───────────────────┐   ┌───────────────────┐
│     TÉCNICAS      │   │  COMPORTAMENTAIS  │   │     CRIATIVAS     │
│ Python, SQL, Cloud│   │Liderança, Riscos  │   │Storytelling, Aulas│
└───────────────────┘   └───────────────────┘   └───────────────────┘ 



```


---




## Normalização de Dicionários Vocabulares
Para evitar redundâncias (como mapear "Desenvolvedor Python", "programar em python" e "Python" como competências distintas), o sistema aplica casamento de padrões semânticos por meio de temperatura controlada ($0.1$) na LLM, mapeando os termos brutos para chaves de tecnologia limpas.


---



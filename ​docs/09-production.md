# 9. Modelo em Produção (Production & Deployment)

## Arquitetura de Microsserviços Containerizados
A solução é totalmente isolada e modularizada utilizando Docker, garantindo que o backend e o frontend funcionem de forma independente tanto em ambientes locais quanto em servidores de nuvem.

---

```

┌────────────────────────┐
│  STREAMLIT DASHBOARD   │ (Porta 8501)
└───────────┬────────────┘
│
(Chamadas HTTP Async)
│
▼
┌────────────────────────┐
│      FASTAPI API       │ (Porta 8000)
└───────────┬────────────┘
│
(JSON Schema Estruturado)
│
▼
┌────────────────────────┐
│   OPENAI AI ENGINES    │ (gpt-4o-mini)
└────────────────────────


```

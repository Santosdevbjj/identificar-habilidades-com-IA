# ==========================================
# Estágio 1: Builder (Compilação e Instalação)
# ==========================================
FROM python:3.11-slim AS builder

WORKDIR /app

# Instala dependências de sistema necessárias para compilar pacotes Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia apenas o arquivo de dependências para aproveitar o cache de camadas do Docker
COPY requirements.txt .

# Instala as dependências isolando-as em um diretório local do usuário
RUN pip install --no-cache-dir --user -r requirements.txt


# ==========================================
# Estágio 2: Runtime (Imagem Final de Produção)
# ==========================================
FROM python:3.11-slim AS runtime

WORKDIR /app

# Variáveis de ambiente para otimização do Python em containers
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH=/root/.local/bin:$PATH

# Copia as dependências instaladas no estágio de build
COPY --from=builder /root/.local /root/.local

# Copia o código-fonte da aplicação respeitando a arquitetura do projeto
COPY src/ /app/src/

# Expõe as portas lógicas da API (8000) e do Dashboard (8501)
EXPOSE 8000
EXPOSE 8501

# Cria um script de inicialização para permitir rodar os dois serviços se necessário,
# ou definir qual serviço subir através de argumentos de linha de comando.
RUN echo '#!/bin/sh\n\
if [ "$SERVICE_TYPE" = "dashboard" ]; then\n\
    exec streamlit run src/dashboard/streamlit_app.py --server.port=8501 --server.address=0.0.0.0\n\
else\n\
    exec uvicorn src.app.main:app --host 0.0.0.0 --port 8000\n\
fi' > /app/entrypoint.sh && chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

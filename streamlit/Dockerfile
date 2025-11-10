FROM python:3.11-slim

# 1) Dependências do sistema (opcional, mas útil)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# 2) Diretório de trabalho
WORKDIR /app

# 3) Instalar dependências primeiro (cache eficiente)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Copiar o resto do projeto
COPY . .

# 5) Expor a porta do Streamlit
EXPOSE 8501
ENV PORT=8501

# 6) Entrypoint
CMD streamlit run app.py --server.port ${PORT} --server.address 0.0.0.0

FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Use este comando para manter o Flask em execução
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
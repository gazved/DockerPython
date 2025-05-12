FROM python:3.11-slim

WORKDIR /app

# Copia TUDO da pasta atual para /app no container
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","-u","./src/main.py"]
# Usa una imagen base con Playwright preinstalado
FROM mcr.microsoft.com/playwright/python:v1.53.0-jammy

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
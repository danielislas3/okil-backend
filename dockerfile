FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del sistema necesarias para PostgreSQL y otras librerías
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    musl-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Actualizar pip antes de instalar dependencias
RUN pip install --no-cache-dir --upgrade pip

# Copiar solo requirements.txt inicialmente para aprovechar el cache de Docker
COPY requirements.txt .

# Instalar las dependencias de Python listadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto al contenedor
COPY . .

# Exponer el puerto para la aplicación
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
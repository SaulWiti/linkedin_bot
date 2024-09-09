# Utiliza una imagen base de Python 3.10
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala las dependencias de Firefox
RUN apt-get update && apt-get install -y firefox-esr

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del proyecto al contenedor
COPY app/ /app/

# Copia el archivo .env al contenedor
COPY .env .env

# Expone el puerto que el contenedor utilizará (si es necesario)
EXPOSE 8000

# Comando para ejecutar tu script principal
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--timeout-keep-alive", "3600"]





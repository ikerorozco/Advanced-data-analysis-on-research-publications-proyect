# Usa una imagen oficial de Python
FROM python:3.10

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios para la instalación de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia solo las carpetas `src` y `data`
COPY src/ src/

# Expone el puerto en el que correrá la app
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "-u", "src/main.py"]


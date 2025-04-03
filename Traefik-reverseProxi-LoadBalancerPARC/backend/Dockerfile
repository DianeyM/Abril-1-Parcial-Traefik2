# 1. Usar una imagen base ligera de Python
FROM python:3.9-alpine

#2. Establecer el directorio de trabajo dentro del contenedor.Crea una carpeta de nombre "app" en la raiz del contenedor. 
WORKDIR /app

#3. Copiar el archivo requirements.txt que contiene las dependencias de Pytho
COPY requirements.txt .

#Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

#4. Copiar el resto del c�digo fuente de la MV al CONTENEDOR, especificamente en el directorio de trabajo (en este caso "app")..
COPY . . 

#5. Exponer el puerto en el que correr� la app
EXPOSE 5000

#6. Commando para ejecutar la aplicaci�n: 
#      *CMD: Esta es una instrucción en el Dockerfile que define el comando que debe ejecutarse cuando el contenedor se inicia. 
#        Solo se puede tener una instrucción CMD en un Dockerfile; si se define más de una, solo se ejecutará la última.
#      *["python", "app.py"]: Este es el comando que se ejecutará cuando el contenedor se inicie. Especifica que se debe usar el 
#        ejecutable python para correr el archivo app.py en el contenedor. Aquí, se está ejecutando la aplicación Flask con python 
#        app.py.
CMD ["python", "app.py"]

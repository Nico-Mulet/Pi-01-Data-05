#utilizamos la imgen del usua tiangolo
FROM tiangolo/uvicorn-gunicorn-fastapi

RUN pip install pandas

#abrimos el puerto que utilizaremos
EXPOSE 80

#copia todo el contenido de la carpeta "./app" hacia el contenedor con la dirección "/app"
COPY ./app /app


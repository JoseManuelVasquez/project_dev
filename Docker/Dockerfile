FROM python:3.11-slim

RUN pip3 install flask redis && \
    groupadd -r demouser && useradd -r -g demouser demouser && \
    mkdir /src && \
    chown -R demouser:demouser /src

USER demouser

WORKDIR /src

COPY . .

RUN pip install flask redis

ENV FLASK_APP=app.py REDIS_HOST=redis

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]

# Construir la imagen: docker build -t flask-app .
# Arrancar antes Redis: docker run -d --name redis-server redis
# Arrancar la app: docker run -d --name flask-app -p 5000:5000 --env REDIS_HOST=redis-server --link redis-server flask-app
# Ejecutar: docker ps
# syntax=docker/dockerfile:1.0

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-2024-06-17 AS builder
WORKDIR /API
COPY ./API/requirements.txt /home/API/requirements.txt
COPY ./API/main.py /home/API/main.py

RUN echo "Atualizando o pip"
RUN pip install --upgrade pip
RUN echo "Instalando Requeriments"
RUN pip install --no-cache-dir --upgrade -r /home/API/requirements.txt
COPY ./API /home/API/
EXPOSE 8080
CMD ["uvicorn","main:app","--host","127.0.0.1","--port","8080", "--workers","4"]



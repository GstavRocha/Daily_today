# syntax=docker/dockerfile:1.0

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-2024-06-17 AS builder
WORKDIR /API
COPY ./API/requirements.txt /API/requirements.txt

RUN echo "Atualizando o pip"
RUN pip install --upgrade pip
RUN echo "Instalando Requeriments"
RUN pip install --no-cache-dir --upgrade -r /API/requirements.txt
COPY ./API /API/
CMD ["uvicorn","main:app"]




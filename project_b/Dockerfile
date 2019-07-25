FROM python:latest

WORKDIR /root/.pip
COPY ./pip.conf .

WORKDIR /project_b
COPY ./ ./

RUN pip install -r requirements.txt

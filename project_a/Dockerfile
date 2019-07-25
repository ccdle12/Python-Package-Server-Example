FROM python:latest

WORKDIR /root/.pip
COPY ./pip.conf .

WORKDIR /project_a
COPY ./ ./

RUN pip install -r requirements.txt

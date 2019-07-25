FROM python:latest

WORKDIR /
COPY ./ ./

RUN pip install pypiserver \
    && mkdir /packages \
    && mv /dist/library_example-0.1.tar.gz /packages

CMD ["pypi-server", "-p", "8080", "/packages"]

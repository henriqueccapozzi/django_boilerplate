FROM python:3.9-slim

WORKDIR /work

COPY ./Pipfile ./Pipfile

RUN pip install pipenv && \
    pipenv update && \
    pipenv --bare install --dev --system --deploy
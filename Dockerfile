FROM python:3.9-slim

WORKDIR /work

COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock

RUN pip install pipenv && \
    pipenv --bare install --dev --system --deploy
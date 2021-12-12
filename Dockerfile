FROM python:3.9-slim

WORKDIR /work

COPY ./build_deploy/Pipfile ./Pipfile
COPY ./build_deploy/Pipfile.lock ./Pipfile.lock

RUN pip install pipenv 
RUN pipenv update && \
    pipenv --bare install --dev --system --deploy
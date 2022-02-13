FROM python:3.9-slim

WORKDIR /work

RUN pip install pipenv 

COPY ./Pipfile ./Pipfile

RUN pipenv update 2> /dev/null || \
    echo "====> pipenv update error" && \
    pipenv --bare install --dev --system --deploy
FROM python:3.10-slim

WORKDIR /opt/todolist

ENV PIP_DISABLE_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    PYTHON_PATH=opt/todolist \
    POETRY_VERSION=1.2.0

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && apt-get autoclean && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && pip install "poetry==$POETRY_VERSION"

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev

COPY src/ .

ENTRYPOINT ["bash", "entrypoint.sh"]

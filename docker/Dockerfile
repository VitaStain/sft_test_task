ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim AS base

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends curl \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/apt/lists/* \
    && rm -rf /var/cache/apt/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set poetry environment variables
ENV \
    POETRY_VERSION=1.8.3 \
    POETRY_NO_INTERACTION=true \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

RUN pip install "poetry==$POETRY_VERSION"


RUN --mount=type=cache,target=$POETRY_CACHE_DIR \
    --mount=type=bind,source=poetry.lock,target=poetry.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    poetry install

# Copy the source code into the container.
COPY . .

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD python manage.py runserver 0.0.0.0:8000

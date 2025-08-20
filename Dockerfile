FROM python:3.11

ENV LANGUAGE=C.UTF-8
ENV LC_ALL=C.UTF-8

ENV PYTHONHASHSEED=1
ENV PYTHONUNBUFFERED=1

ENV POETRY_VIRTUALENVS_CREATE=0

ARG NODE_MAJOR=20

RUN apt-get update && apt-get install -y \
    bash-completion \
    curl \
    less \
    libpq-dev \
    netcat-traditional \
    vim

RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /app

COPY ./pyproject.toml ./
COPY ./poetry.lock ./

RUN poetry install --no-root

# Copy application code
COPY app .

CMD ["bin/boot.sh"]

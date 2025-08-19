FROM python:3.11

ENV LANGUAGE=C.UTF-8
ENV LC_ALL=C.UTF-8

ENV PYTHONHASHSEED=1
ENV PYTHONUNBUFFERED=1

ARG NODE_MAJOR=20

RUN apt-get update && apt-get install -y \
    bash-completion \
    curl \
    less \
    libpq-dev \
    netcat-traditional \
    vim

RUN pip install --upgrade pip
RUN pip install uv

# Work in /app so uv creates .venv there
WORKDIR /app

# Copy project metadata first for better caching
COPY ./pyproject.toml ./

# Install dependencies into /app/.venv
RUN uv sync

# Ensure venv binaries are on PATH for runtime
ENV PATH="/app/.venv/bin:$PATH"

# Copy application code
COPY app /app
RUN mkdir -p /app/static

CMD ["bin/boot.sh"]

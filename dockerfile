# Base image with Python
FROM python:3.12-slim as builder-base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.0 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Prepend poetry to path
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set working directory
WORKDIR /app

# Copy project dependency files
COPY poetry.lock pyproject.toml ./

# Install project dependencies
RUN poetry install --no-dev

# Copy the entire project directory
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

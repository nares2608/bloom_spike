# Base Python image
FROM python:3.13-alpine

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_VERSION=0.8.5

# Install system dependencies
RUN apk update && apk add --no-cache \
    curl \
    build-base \
    git \
    libffi-dev \
    openssl-dev \
    postgresql-dev \
    musl-dev \
    gcc \
    cargo \
    nodejs \
    npm \
    bash  # optional, useful for shell access

# Install UV
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy only requirements to cache dependencies
COPY pyproject.toml uv.lock /app/

# Install project dependencies
RUN uv pip install --system --no-cache .

# Copy entrypoint
COPY deploy/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy project code
COPY src/ /app/

# Expose port
EXPOSE 80

# Entrypoint & default command
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "bloom/manage.py", "runserver", "0.0.0.0:80"]

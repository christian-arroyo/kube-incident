FROM ghcr.io/astral-sh/uv:python3.12-trixie-slim

WORKDIR /app

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1
# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Omit development dependencies
ENV UV_NO_DEV=1

# Installing separately from its dependencies allows optimal layer caching
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

COPY app/ .
EXPOSE $FASTAPI_RUN_PORT

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

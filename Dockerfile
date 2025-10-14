ARG BASE_IMAGE=python:3.12.0-slim-bullseye
FROM $BASE_IMAGE

# Use the uv binary
COPY --from=ghcr.io/astral-sh/uv:0.6.6 /uv /bin/uv

# Allows the container to start up faster.
ENV UV_COMPILE_BYTECODE=1

# Set working directory as `/code/`
WORKDIR /code

# Copy project packages & dependcies
COPY pyproject.toml /code/pyproject.toml
COPY uv.lock /code/uv.lock

# Install uv via pip, then install all packages.
# https://docs.astral.sh/uv/reference/cli/#uv-sync
RUN pip install --no-cache-dir --upgrade pip==25.2 && \
    uv sync --locked

# Copy application code to `/code/app/`
COPY config.py main.py prompts.py /code/app/

# Run application using `uv`
CMD ["uv", "run", "/code/app/main.py"]

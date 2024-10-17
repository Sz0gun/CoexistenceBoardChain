# Stage 1: Build
FROM python:3.9-slim AS builder
WORKDIR /app
COPY pyproject.toml .
RUN pip install poetry && poetry install

# Stage 2: Production
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY ./backend /app/backend
COPY ./config /app/config
EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info"]
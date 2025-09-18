# Stage 1: Build stage
FROM python:3.9-slim AS builder
WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install dependencies
COPY requirements.txt constraints.txt ./
RUN pip install --upgrade pip \
    && pip install "setuptools==58.0.0" \
    && pip install --prefix=/install -r requirements.txt

# Stage 2: Final image
FROM python:3.9-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 PORT=8000

# Copy installed packages
COPY --from=builder /install /usr/local

# Copy app code
COPY . .

EXPOSE $PORT
CMD ["gunicorn", "pp4_pizzatheaction.wsgi", "--bind", "0.0.0.0:8000"]

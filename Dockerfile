# ============================
# Stage 1: Builder
# ============================
FROM python:3.9-slim AS builder

# Set working directory
WORKDIR /app

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Copy requirements first for caching
COPY requirements.txt constraints.txt ./

# Upgrade pip, downgrade setuptools (needed for old django-allauth), install dependencies to /install
RUN pip install --upgrade pip \
    && pip install "setuptools==58.0.0" \
    && pip install --prefix=/install -r requirements.txt

# ============================
# Stage 2: Final runtime image
# ============================
FROM python:3.9-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8000

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy the application code
COPY . .

# Expose the Heroku port
EXPOSE $PORT

# Start the app with Gunicorn
CMD ["gunicorn", "pp4_pizzatheaction.wsgi", "--bind", "0.0.0.0:8000", "--workers", "3"]

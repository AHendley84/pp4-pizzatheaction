# Use Python 3.9 slim base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8000

# Set working directory
WORKDIR /app

# Upgrade pip and downgrade setuptools for old django-allauth
RUN pip install --upgrade pip \
    && pip install "setuptools==58.0.0"

# Copy only the dependency files first to leverage Docker cache
COPY requirements.txt constraints.txt ./

# Install dependencies in a single layer
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port
EXPOSE $PORT

# Use JSON array for CMD to prevent shell issues with signals
CMD ["gunicorn", "pp4_pizzatheaction.wsgi", "--bind", "0.0.0.0:8000"]

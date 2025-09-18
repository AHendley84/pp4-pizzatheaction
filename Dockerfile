# Use Python 3.9 slim base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8000

# Set working directory
WORKDIR /app

# Copy requirements and constraints first (for caching)
COPY requirements.txt constraints.txt ./

# Downgrade setuptools first (required for old django-allauth)
RUN pip install "setuptools==58.0.0"

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port (Heroku uses $PORT env var)
EXPOSE $PORT

# Command to run app
CMD gunicorn pp4-pizzatheaction.wsgi --bind 0.0.0.0:$PORT

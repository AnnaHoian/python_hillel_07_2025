# Base Python image
FROM python:3.11-slim

# Folder in container for code
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir sqlalchemy psycopg2-binary

# Default command when starting container
CMD ["python", "test_app.py"]
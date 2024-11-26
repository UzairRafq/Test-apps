# Base Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  # Prevent Python from writing .pyc files
ENV PYTHONUNBUFFERED 1        # Prevent Python from buffering stdout and stderr

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the Django project
COPY . .

# Expose the port the app runs on
EXPOSE 8008

# Set the default command to run Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8008"]

# Use official Python image
FROM registry-1.docker.io/library/python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for OpenCV)
RUN apt-get update && apt-get install -y \
    libgl1 libglib2.0-0 && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run detect.py by default with a folder argument
CMD ["python", "detect.py","test/images"]

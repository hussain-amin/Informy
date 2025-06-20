# Use official Python image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source files
COPY . .

# Make reports directory available as volume (optional)
VOLUME ["/app/reports"]

# Set entrypoint to run main.py by default
ENTRYPOINT ["python", "main.py"]

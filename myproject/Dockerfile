# Use official Python image
FROM python:3.11-slim

# Set up working directory
WORKDIR /app

# Copy dependency files
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project to container
COPY . /app/

# Open port for Django
EXPOSE 8000

# Server startup command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

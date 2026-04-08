# Use the official Python image with a slim variant
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install FastAPI, Uvicorn, and any other dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files
COPY . .

# Expose the application port
EXPOSE 8000

# Run the application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
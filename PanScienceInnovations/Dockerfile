# Use official Python image
FROM python:3.12.4

# Set working directory
WORKDIR /app

# Copy application files
COPY app/ /app/

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 9999

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9999"]
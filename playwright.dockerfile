FROM mcr.microsoft.com/playwright/python:v1.35.0-jammy

# Set work directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run script
CMD ["python", "main.py"]

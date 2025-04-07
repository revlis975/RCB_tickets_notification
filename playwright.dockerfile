# Use Playwright's official Python image with browsers already installed
FROM mcr.microsoft.com/playwright/python:v1.43.0-jammy

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

CMD ["python", "main.py"]

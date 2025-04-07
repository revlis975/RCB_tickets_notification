FROM mcr.microsoft.com/playwright/python:v1.43.0-jammy

WORKDIR /app

# Copy your app's dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

CMD ["python", "main.py"]

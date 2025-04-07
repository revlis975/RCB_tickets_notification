FROM mcr.microsoft.com/playwright/python:v1.42.1-jammy

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]

FROM python:3.11-slim

# Avoid prompts from tzdata
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

# System dependencies for Playwright
RUN apt-get update && apt-get install -y wget gnupg ca-certificates \
    libnss3 libatk-bridge2.0-0 libxss1 libasound2 libx11-xcb1 \
    libxcomposite1 libxdamage1 libxrandr2 libgbm1 libgtk-3-0 \
    libpango-1.0-0 libpangocairo-1.0-0 fonts-liberation libxext6 \
    libxfixes3 libxi6 libxtst6 libcurl4 unzip curl && apt-get clean

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN python -m playwright install --with-deps

# Copy the rest of the code
COPY . .

CMD ["python", "main.py"]

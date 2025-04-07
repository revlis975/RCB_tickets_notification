# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set workdir
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget gnupg ca-certificates fonts-liberation libnss3 libxss1 libasound2 libatk-bridge2.0-0 \
    libgtk-3-0 libx11-xcb1 libxcb1 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libpango-1.0-0 \
    libpangocairo-1.0-0 libxext6 libxfixes3 libxi6 libxtst6 libwayland-client0 libwayland-cursor0 \
    libwayland-egl1 libcurl4 tzdata unzip

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Playwright browsers
RUN pip install playwright && playwright install --with-deps

# Copy project
COPY . .

# Run your script (replace with your actual script)
CMD ["python", "main.py"]

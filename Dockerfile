# Base image from official Python with Debian (compatible with Playwright)
FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget gnupg curl \
    libnss3 libxss1 libasound2 libatk1.0-0 libatk-bridge2.0-0 libcups2 \
    libdbus-1-3 libgdk-pixbuf2.0-0 libgtk-3-0 libxcomposite1 libxdamage1 \
    libxrandr2 libgbm1 libxshmfence1 libx11-xcb1 libxrender1 libxext6 \
    libxfixes3 libx11-6 libxau6 libxdmcp6 libxinerama1 libxkbcommon0 \
    libpangocairo-1.0-0 fonts-liberation && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Playwright + Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && playwright install --with-deps

# Copy the rest of your code
COPY . .

# Run script
CMD ["python", "main.py"]

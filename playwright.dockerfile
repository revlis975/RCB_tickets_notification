FROM debian:bullseye

# Avoid tzdata prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system deps
RUN apt-get update && apt-get install -y \
    curl wget gnupg unzip python3 python3-pip python3-venv \
    libnss3 libatk-bridge2.0-0 libxss1 libasound2 libx11-xcb1 \
    libxcomposite1 libxdamage1 libxrandr2 libgbm1 libgtk-3-0 \
    libpango-1.0-0 libpangocairo-1.0-0 fonts-liberation libxext6 \
    libxfixes3 libxi6 libxtst6 libcurl4 ca-certificates && apt-get clean

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Install compatible Playwright version + deps
RUN python3 -m playwright install --with-deps

# Copy code
COPY . .

# Run app
CMD ["python3", "main.py"]

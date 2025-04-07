FROM python:3.10-slim

RUN apt update && apt install -y wget gnupg curl \
    libnss3 libxss1 libasound2 libatk1.0-0 libatk-bridge2.0-0 libcups2 \
    libdbus-1-3 libgdk-pixbuf2.0-0 libgtk-3-0 libxcomposite1 libxdamage1 \
    libxrandr2 libgbm1 libxshmfence1 libx11-xcb1 libxrender1 libxext6 \
    libxfixes3 libx11-6 libxau6 libxdmcp6 libxinerama1 libxkbcommon0 \
    libpangocairo-1.0-0 fonts-liberation && \
    pip install --no-cache-dir -r requirements.txt && \
    playwright install --with-deps

WORKDIR /app
COPY . .

CMD ["python", "main.py"]
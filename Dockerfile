# Используем образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем приложение
COPY app.py .

# Устанавливаем Chrome и драйвер ChromeDriver
RUN apt-get update && apt-get install -y wget gnupg2 && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    wget -q "https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip" && \
    unzip chromedriver_linux64.zip -d /usr/local/bin/ && \
    rm chromedriver_linux64.zip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Указываем команду запуска приложения
CMD ["python", "app.py"]

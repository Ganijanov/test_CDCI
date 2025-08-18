FROM python:3.11-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Рабочая директория
WORKDIR /app

# Скопировать зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать весь проект
COPY . /app/

# Запускаем сервер (или тесты в CI)
CMD ["gunicorn", "conf.wsgi:application", "--bind", "0.0.0.0:8000"]

FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    --fix-missing \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app/event_manager

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

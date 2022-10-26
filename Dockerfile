FROM python:3.9-slim

ENV HOME /app
WORKDIR /app

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .
CMD python manage.py runserver 0.0.0.0:8000

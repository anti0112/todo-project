FROM python:3.10-slim

ENV HOME /app
WORKDIR /app

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .
CMD python3 -m ./todolist/manage.py runserver

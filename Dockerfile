FROM python:3.10-slim

ENV HOME /app
WORKDIR /app

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .
CMD python -m ./todolist/manage.py runserver.py

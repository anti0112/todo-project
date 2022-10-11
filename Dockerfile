FROM python:3.9-slim


WORKDIR /app/todolist

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .
CMD [ "sh", "entrypoint.sh" ]

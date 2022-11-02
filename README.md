### 1. Создать виртуальное окружение, активировать его и установить зависимости
```shell
virtualenv venv
```
```shell
source venv/Scripts/activate
```
```shell
pip install -r requirements.txt
```
### 2. Заполнить файл .env.example нужными данными
### 3. Создаем контейнеры требующиеся для работы программы
```shell
docker-compose up -d
```
### В проекте уже настроенно подлючение к базе данных созданной через docker-compose,



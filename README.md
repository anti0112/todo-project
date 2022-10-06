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
### 2. Создаем контейнер с базой данных Postgresql с помощью команды:
```shell
docker-compose up -d
```
### В проекте уже настроенно подлючение к базе данных созданной через docker-compose,
### 3. Выполнить миграции
```shell
./manage.py migrate
```

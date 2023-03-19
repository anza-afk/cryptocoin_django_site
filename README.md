# Cryptocoin APP
____
### Установка:

Клонируем проект:

    git clone https://gitlab.com/anza-afk/apptrix_test

## Запуск проекта с помощью Docker:

Создать .env файл в корневой директории и заполнить его по примеру .env.example из корня проекта

### Выполнить в корне проекта:

    docker-compose -f docker-compose.yml up -d --build
    docker-compose -f docker-compose.yml exec web python manage.py makemigrations --noinput
    docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
    docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear
    docker-compose -f docker-compose.yml exec web python manage.py createsuperuser

____ 
### API:

Для наглядности в API не выключен JSONRenderer, чтобы было проще проверить всё.  

    endpoint /api/v1 ведёт в корень API (API root)  
    endpoint /api/v1/cryptocurrencies/ ведёт на список всех криптовалют  
    endpoint'ы /api/v1/cryptocurrencies/<name>, /api/v1/cryptocurrencies/<symbol> и /api/v1/cryptocurrencies/<id>  
    ведут на конеретную криптовалюту, если таковая найдётся (поиск сразу по 3 полям)  
    endpoint /api/v1/users/ ведёт на список всех пользователей  
    endpoint /api/v1/users/<pk> ведёт на конкретного пользователя  

____
### NB
Из-за ограничений Coinmarketcap API на количество запросов (333 кредитов в день, на запрос всех 9060 валют потребовалось бы 46 кредитов), в ENV выставлен ограничитель в 400 криптовалют в переменной LIMIT

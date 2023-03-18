import json
import requests
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import date, timedelta
from .models import Cryptocurrency
from django.core.paginator import Paginator


def get_paginated_query(request, crypto_data):
    paginator = Paginator(crypto_data, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def put_data_to_db(crypto_clean_data: list[dict]) -> None:
    for currency in crypto_clean_data:
        db_currency, created = Cryptocurrency.objects.update_or_create(
            name=currency['name'],
            defaults=currency
        )


def get_clean_data(crypto_data: list[dict]) -> list[dict]:
    model_data = (
        'name',
        'symbol',
        'circulating_supply'
        )
    price_data = (
        'price',
        'percent_change_24h',
        'volume_24h',
        'percent_change_7d'
    )
    crypto_clean_data = []
    for currency in crypto_data:
        crypto_dict = {key: currency[key] for key in model_data}
        price_dict = {key: currency['quote']['USD'][key] for key in price_data}
        crypto_dict.update(price_dict)
        crypto_clean_data.append(crypto_dict)
    return crypto_clean_data


def get_crypto_from_api(api_key: str, limit: int = 200) -> list[dict]:
    url = (
        'https://pro-api.coinmarketcap.com/'
        'v1/cryptocurrency/listings/'
        f'latest?start=1&limit={limit}&convert=USD'
    )

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        data = json.loads(response.text)
        res = [item for item in data['data']]
        return res
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return []


def get_crypto_news(api_key: str) -> list[dict]:
    today = date.today()
    yesterday = today - timedelta(days=1)
    url = (
        f'https://newsapi.org/v2/everything?'
        'q=Cryptocurrency&'
        f'from={yesterday}&'
        f'to={today}'
        'sortBy=popularity&'
        f'apiKey={api_key}'
    )
    try:
        response = requests.get(url)
        res = [article for article in response.json()['articles']]
        return res
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return []

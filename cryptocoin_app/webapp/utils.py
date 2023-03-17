import json
import requests
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import date, timedelta


def get_all_crypto(api_key: str, limit: int=200) -> list[dict]:
    url = ('https://pro-api.coinmarketcap.com/'
        'v1/cryptocurrency/listings/'
        f'latest?start=1&{limit}&convert=USD')

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
        # with open('listings-latest-test2.txt', 'w', encoding="UTF-8") as file:
        #     for item in data['data']:
        #         file.write(f'{item}\n')
        return res
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def get_crypto_news(api_key: str) -> list[dict]:
    today = date.today()
    yesterday = today - timedelta(days=1)
    url = (f'https://newsapi.org/v2/everything?'
       'q=Cryptocurrency&'
       f'from={yesterday}&'
       f'to={today}'
       'sortBy=popularity&'
       f'apiKey={api_key}')
    try:
        response = requests.get(url)
        res = [article for article in response.json()['articles']]
        return res
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
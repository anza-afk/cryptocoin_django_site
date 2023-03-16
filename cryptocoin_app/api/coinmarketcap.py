API_KEY = '46177aad-2317-4569-8f01-9fd2abc64a16'
PRO_API_URL = 'pro-api.coinmarketcap.com'
MOCK_API_KEY = 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'
MOCK_API_URL = 'sandbox-api.coinmarketcap.com'

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = f'https://{MOCK_API_URL}/v1/cryptocurrency/listings/latest'
parameters = {
  'limit': '200',
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': MOCK_API_KEY,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url)
    data = json.loads(response.text)
    with open('listings-latest-test.txt', 'w', encoding="UTF-8") as file:
        for item in data['data']:
            file.write(f'{item}\n')
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


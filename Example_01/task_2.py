# Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

# Выбран holidays.abstractapi.com - праздничные дни по дате
import json
from pprint import pprint

import requests

with open('api_key.json', 'r') as f:
    data = json.load(f)
    api_key = data['api_key']

url = 'https://holidays.abstractapi.com/v1/'
params = {
    'api_key': api_key,
    'country': 'RU',
    'year': '2021',
    'month': '01',
    'day': '01'
}

response = requests.get(url, params=params)
# pprint(response.json())

with open('task_2.json', 'w') as f:
    f.write(response.text)

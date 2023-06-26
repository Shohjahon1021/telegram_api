import requests
from pprint import pprint

TOKEN = '5758535081:AAGYdZ2rSo-r0_l-liwWe8CnKHigWSnItjY'
url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
response = requests.get(url)
data = response.json()
updates = data['result']
for update in updates:
    messenge = update['message']
    user = messenge['from']
    pprint(user)


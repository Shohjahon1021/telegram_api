import requests
from pprint import pprint

TOKEN = '5758535081:AAGYdZ2rSo-r0_l-liwWe8CnKHigWSnItjY'
url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
response = requests.get(url)
data = response.json()
updates = data['result']

# user_id = 1333107837

for update in updates:
    messenge = update['message']
    user = messenge['from']
    user_id = user['id']
    frist = user.get('first_name','')
    last = user.get('last_name','')

    print(user_id,end=',')


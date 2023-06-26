import requests
from pprint import pprint as pp

def sendMessage(idx):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id':idx,
        'text':'Assalomu aleykum'
    }
    response = requests.get(url,params=payload)
TOKEN = '5758535081:AAGYdZ2rSo-r0_l-liwWe8CnKHigWSnItjY'
# data = response.json()
ids = [1333107837,1836864008]
for idx in ids:
    sendMessage(idx)



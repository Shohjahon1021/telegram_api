import requests
from pprint import pprint

def sendMessage(idx,text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    paylode = {
        'chat_id':idx,
        'text':text
    }
    response = requests.get(url,params=paylode)

TOKEN = '5758535081:AAHSsYRtJF2Lsz43dlTfct5pZ0DZ-LkeEGM'
url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
response = requests.get(url)
data = response.json()
text = data['result'][-1]['message']['text']
print(text)
ids = [1333107837,1836864008]
for idx in ids:
    sendMessage(idx,text)


import requests
from pprint import pprint

TOKEN = '5758535081:AAGYdZ2rSo-r0_l-liwWe8CnKHigWSnItjY'
url = f'https://api.telegram.org/bot{TOKEN}/sendMessenge'
response = requests.get(url)
data = response.json()



# user_id = 1333107837



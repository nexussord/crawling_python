import json
import os
import requests
from bs4 import BeautifulSoup

# python file location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://www.fmkorea.com/hotdeal')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# my_hotdeals is list type
my_hotdeals = soup.select('h3 > a')
my_hotdeals_info = soup.select('div.hotdeal_info')

data = {}

# for hotdeals in my_hotdeals:
#     print(hotdeals.text)

# for price in my_hotdeals_info:
#     print(price.text)

for hotdeals, info in zip(my_hotdeals, my_hotdeals_info):
    data[hotdeals.text] = info.text
    # print(hotdeals.text, info.text)

with open(os.path.join(BASE_DIR, 'hotdeal.json'), 'w+', encoding='UTF-8-sig') as json_file:
    # korean language saved as unicode; using ensure_ascii=False fixes it
    json.dump(data, json_file, ensure_ascii=False)


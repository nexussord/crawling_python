import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.fmkorea.com/hotdeal')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

## my_hotdeals is list type
my_hotdeals = soup.select('h3 > a')
my_hotdeals_info = soup.select('div.hotdeal_info')



# for hotdeals in my_hotdeals:
#     print(hotdeals.text)
#
# for price in my_hotdeals_info:
#     print(price.text)

for hotdeals, info in zip(my_hotdeals, my_hotdeals_info):
    print(hotdeals.text, info.text)


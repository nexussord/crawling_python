import requests
from bs4 import BeautifulSoup
import json
import os

## python file location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

## HTTP GET Request
req = requests.get('https://www.murung.site')

## crawl HTML source
html = req.text

## crawl HTTP header
## header = req.headers

## bring HTTP status (200 : normal)
## status = req.status_code

## check if HTTP works fine (True/False)
## is_ok = req.ok

## change html source into python elements
## BeautifulSoup(html source, choose which parser to use)
soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    'a'
)

data = {}

for title in my_titles:
    data[title.text] = title.get('href')

print(data)

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)



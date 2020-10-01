import requests
from bs4 import BeautifulSoup

## HTTP GET Request
req = requests.get('https://www.murung.site')

## crawl HTML source
html = req.text

## crawl HTTP header
header = req.headers

## bring HTTP status (200 : normal)
status = req.status_code

## check if HTTP works fine (True/False)
is_ok = req.ok

## change html source into python elements
## BeautifulSoup(html source, choose which parser to use)
soup = BeautifulSoup(html, 'html.parser')

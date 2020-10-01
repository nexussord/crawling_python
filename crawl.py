import requests

## HTTP GET Request
req = requests.get('https://www.murung.site')

## crawl HTML source
html = req.text

## crawl HTTP header
header = req.headers

## bring HTTP status (200 : normal)
status = req.status_code

## Check if HTTP works fine (True/False)
is_ok = req.ok

print(header)
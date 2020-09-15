#!/bin/python3

import requests                 # pip3 install requests
from bs4 import BeautifulSoup   # pip3 install bs4


url = 'https://www.python.org'
html = requests.get(url,
                    headers={
                        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
                    })
html.raise_for_status()  # stops script if http status != 200
soup = BeautifulSoup(html.text, features="html.parser")
# print events in format: DATE EVENT LINK
for event in soup.select('.event-widget li'):
    print(f'{event.time.get("datetime")[:10]}\t{event.a.text.ljust(30)}{url + event.a.get("href")}')

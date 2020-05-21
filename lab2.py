import urllib
import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import socks
import socket
socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket

URL = f"https://news.yandex.ru/yandsearch?rpt=nnews2&grhow=clutop&from=tabbar&text=american%20news"


def f():

    r = []
    resp = requests.get(URL, headers={'User-Agent': UserAgent(use_cache_server=False, cache=False).random})
    soup = BeautifulSoup(resp.content, "html.parser")

    ganich = soup.find('ul', attrs={'class': 'search-list search-list_group_yes'})
    for g in ganich.find_all('li', attrs={'class': 'search-item'}):
        name_ = g.find('div', attrs={'class': 'document__provider-name'})
        header_ = g.find('div', attrs={'class': 'document__title'})
        snippet_ = g.find('div', attrs={'class': 'document__snippet'})

        print(name_.text, header_.text, snippet_.text, sep='\n')
        print()
        if ('Трамп' or 'Trump') in header_.text:
            r.append((name_.text,header_.text,snippet_.text))
    return r

t = time.time() + 24*60*60

last_ = set(f())
results = [*last_]

import random
while t - time.time() >= 0:

    last_n = set(f())
    results.append(last_n-last_)
    last_ = last_n

    time.sleep(360 + random.randint(0, 100))

# my commit
print(*results)

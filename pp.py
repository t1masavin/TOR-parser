
import requests
from bs4 import BeautifulSoup as bs

a_link = requests.get('https://en.wikipedia.org/wiki/Special:Random').url
b_link = requests.get('https://en.wikipedia.org/wiki/Special:Random').url

a_to_b = []

def tr_or(link):
    if link.get('href'):
        if link.get('href')[:5] == 'https':
            return True
        else:
            return False
    else:
        return False

def back_(link):
    ff = [link]
    for i in a_to_b[::-1]:
        link = i[link]
        ff.append(link)
    print(ff)

def forw(a_link):
    a_to_b.append({a_link: '<PAD>'})
    for i in range(10):
        a_to_b.append({})
        for k in a_to_b[-2].keys():
            link_s = bs(requests.get(k).content, 'html.parser')
            link_s = link_s.find_all('a')
            link_s = [link.get('href') for link in link_s if tr_or(link)]

            for link in link_s:
                if link == b_link:
                    return back_(k)
                a_to_b[-1][link] = k
    print('Нет цепи из a в b')

forw(a_link)

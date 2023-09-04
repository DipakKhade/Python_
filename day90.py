# Exercise 10: News App in Python | Python Tutorial - Day #90

import requests
from bs4 import BeautifulSoup

url='38217c6a17884b52965090549c34b4f3'

r=requests.get(url)
soup=BeautifulSoup(r.text,'html.perser')
print(soup)
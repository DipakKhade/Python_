# Requests Module in Python | Python Tutorial - Day #89

import requests
from bs4 import BeautifulSoup

# request for wesite code
# responce=requests.get('http://google.com')
# print(responce.text)

# for beautifying

url='http://www.mindmiracles.in/'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')

for heading in soup.find_all('h2'):
    print(heading.text)

# Exercise 10 - News App Solution & Shoutout | Python Tutorial - Day #93

import requests
import json


query=input('What type of news are you interested in ? ')
url=''
r=requests.get(url)
print(r.text)

news=json.loads(r.text)

# using for loop


# MultiProcessing in Python | Python Tutorial - Day #98

import multiprocessing
import requests


def downloadFile(url,name):
    print('The downoading is started {name}')
    response=requests.get(url)
    open(f'file{name}.jpg','wb').write(response.content)
    pass
    print(f'downloading is finshed {name}')


url='https://picsum.photos/2000/3000'

for i in range(5):
    downloadFile(url,i)

# The above process using multipocessing

pros=[]
p=multiprocessing.Process(target=downloadFile,args=[url,i])

p.start()
pros.append(p)

for p in pros:
    p.join()

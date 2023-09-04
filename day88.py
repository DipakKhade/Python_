# Exercise 9: Solution - Shoutouts to Everyone | Python Tutorial - Day #88

from text_to_speech import save

list=['Dipak','Gauarv','Krushna']

for list in list:

    save(f'shoutout to {list}','en',file='shoutout_day88.mp3')
    list=list+1



## Dictionaries in python

#Dictionaries use to create a mapping

d={'Dipak': 'me',
     'Gaurav':'friend',
     'Nimbodi':'village'
   }

print(d['Dipak'])

for i in d:
    print(i)

print(d)



#these two are the same things

print(d['Dipak'])             #if key is not exist then this will throw a error
print(d.get('Dipak'))          #if key is not exist then this will give a none output



#to accees the all the keys

print(d.keys())
print(d.values())

#or
print(d.items())

#or
for keys in d.keys():
    print(keys)




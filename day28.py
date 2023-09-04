# f-strings in Python | Python Tutorial - Day #28


#string formatting
about='My name is {} and im learning {}'

name='Dipak'
learn='Python'

d=about.format(name,learn)
print(d)


# f string
# we can add a varable in string by using f string

about1=f'My name is {name} and im learing {learn} '
print(about1)

str1=f'{2*6}'
print(str1)


clg='Modern'
print(f'my college name is {clg}')
print(f'my college name is {{clg}}')

print(f'my collage name is to be {clg}')


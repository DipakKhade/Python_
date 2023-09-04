# Introduction to Lists in Python | Python Tutorial - Day #22

marks=[12,18,10,6,17]
print(type(marks))
print(marks[0])
print(marks[-3])

if 12 in marks:
    print('yes')
else:
    print('no')

for marks in marks:
    print(marks)

lst=[i*i for i in range(10)]
print(lst)

lst=[i*i for i in range(10) if i%2==0]
print(lst)












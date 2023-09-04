# For Loops in Python | Python Tutorial - Day #17


# iterating elements in string
name='Dipak'
for i in name:
    print(i)
    if i=='D':
        print('This is D')

# iterating elements in list

friends=['Vishal','Aniket','Avinash','Omkar']

for friends in friends:
    print(friends)

    for i  in friends:
        print(i)

#printing numbers using range function

for k in range(101):
     print(k)

# or 
for d in range(1,10):
    print(d)

for g in range(1,20,2):   # range (n,n-1,d)
    print(g)

    
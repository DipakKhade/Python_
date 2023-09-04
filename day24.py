# Tuples in Python | Python Tutorial - Day #24

#tuples are immutable i.e it can not changes

tup=(1,34,5,6,6,9)
print(tup)
# to make a tuple of single element
tup1=(7,)
print(type(tup1))

print(tup[0])  # indexing are same as list

if 5 in tup:
    print('yes it is  is present')
else:
    print('it is not present')

newtup=tup[0:2]
print(newtup)

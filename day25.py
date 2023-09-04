# Operations on Tuples in Python | Python Tutorial - Day #25

# Tuples are immutable , hance if you want to add,remove or change tuple items ,then first you must convert the tuple to a list . Then perform operation on that list and convert it back to tuple


tup=(1,2,4,5,9)
lst=list(tup)
print(lst)
lst.append(100)

tup2=tuple(lst)
print(tup2)

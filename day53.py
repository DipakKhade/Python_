# Map, Filter and Reduce in Python

def cube(x):
    return x*x*x

list1=[2,3,4,5,6]



# newlist=[]
# for item in list1:
#     newlist.append(cube(item))
# print(newlist)


# MAP
# The above should be done by using Map 

newlist=list(map(cube,list1))
print(newlist)

'''here we also use a lambda function'''
# newlist=list(map(lambda x:x*x*x,list1))
# print(newlist)


# FILTER

def filter_function(a):
    return a>4

newnewl=list(filter(filter_function,list1))
print(newnewl)


#REDUCE

from functools import reduce

numbers=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y , numbers)
print(sum)


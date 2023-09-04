## set methods

a={1,2,4,7,8}
b={9,8,1,5}

print(a.union(b))

a.update(b)
print(a)

print(a.intersection(b))

a.intersection_update(b)  #make changes in original set


#symmetric difference 
#values which are not comman    i.e   a union b - a intersection b
c=a.difference(b)
print(c)

#disjoint set   i.e  intersection is empty
print(a.isdisjoint(b))

print(a.issuperset(b))

print(a.issubset(b))

#to add a single item to a set
a.add(45)
print(a)

#to remove the item
a.remove(1)
print(a)

#use discard to remove the items   beacuse it can give the error when the item is not present in set
a.discard(9)
print(a)

#POP
#this pops out a random element from a set
p=a.pop()
print(p)

#del
#this is a keyword to delete the set
del a

#clear
#to clear the all elements in set








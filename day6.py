# Variables and Data Types

a=7
print(a)

b="dipak"
print(b)

c=9
print(c)
print(type(c))
print(type(a))

print("this is the value",a+c)

d=complex(2,7)
print(type(d))

list1=["dipak","prajyot",[2,3,123,9],9]
print(list1[1])

tupple=(21,223,2,"dipak")
print(tupple)
print(type(tupple))
print(tupple[1])

dict1={
    "dipak":"good boy",
    "prajyot":"is aslo a good boy"


}
print(dict1)
print(type(dict1))
print(dict1["dipak"])

input=input("enter the name:")
print(dict1.get(input))

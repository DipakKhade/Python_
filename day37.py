##Finally Keyword in python


def func1():

    try:

       l=[1,2,3,4]
       i=int(input('Enter the index : '))
       print(l[i])
       return 1
    except:
       print('there is a error')
       return 0
    finally:
       print('This is always executed')   
       

x=func1()
print(x)

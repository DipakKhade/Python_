# Function Arguments in Python | Python Tutorial - Day #21

'''def average(a,b):
    print('The average is :',(a+b)/2)

average(100,200)

def average(a=5,b=8):
    print('The average is :',(a+b)/2)

average()'''


def ave(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        print(sum/len(numbers))

ave(1,2)


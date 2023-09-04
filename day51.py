# seek(), tell() and other functions

with open('Dipak8999.txt','r') as f:
    print(type(f))

    f.seek(4)              #seek the cursor to to 4th position

    # f.truncate(18)          #file will contain only first 18 char.
    
    data=f.read(2)          #read the 2 char. from seek position
    print(data)


    
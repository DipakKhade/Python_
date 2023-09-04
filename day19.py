# break and continue in Python | Python Tutorial - Day #19

for i in range (11):
    if i==5:
        print('The itration has been skiped')
        continue
    
    
    
    print(i)

print('The loop has been ended')


#infinite loop
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break


    
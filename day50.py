# read(),readlines() and other methods

f=open('Dipak8999.txt','rt')
content=f.read()
print(content)

line=f.readlines()

f.close()

# while True:
#     line=f.readline()
#     print(line)
#     if not line:
#         break
#     print(line)

lines=['Dipak \n','Gaurav \n','DK \n']
f2=open('name','w')
f2.writelines(lines)



str_ = input("Enter the String")
e = str_.split(' ')
count= 0
#print(e)
for x in range(0,len(e)):
    #print(e[x])
    if e[x]=='':
        count +=1
    #print(e)
print(len(e)-count)
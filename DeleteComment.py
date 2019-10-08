import re
print("enter file name to read")
var1=input()
fd=open(var1)
fd1=open('update.txt','w+')
var2=fd.readline()
while var2 !='':
    obj=re.finditer('\A[^#\n]',var2)
    #print (obj)
   # if obj:
    #    print ("True")
    for match in obj:
       # print (match.group())
        #if match.group()!="#":
        fd1.write(var2)
    var2=fd.readline()
fd1.close()
fd1=open('update.txt')
print(fd1.read())

#can tryy by using .search
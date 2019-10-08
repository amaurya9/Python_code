import re
print("Enter a string for pattern match and pattern")
str1=input()
#pattern=input()
'''obj=re.match(pattern,str1)
if obj:
    print ("match found in between ({},{})".format(obj.start(),obj.end()))
else:
    print ("match not found")
#str3=list(str1)
#print (str3)
#str2=str3.reverse()
#print (str3[::-1])
#print (str1)
str1=str1[::-1]
obj=re.match(pattern,str1)
if obj:
    print ("match found in between ({},{})".format(obj.start(),obj.end()))
else:
    print ("match not found")
obj = re.findall(pattern,str1)
#count=0
#for x in obj:
#    count+=1
print ("Occurence is {}".format(len(obj)))
print ("enter a string to replace the pattern")
ReplaceBy=input()
str2=re.sub(pattern,ReplaceBy,str1)
print ("Replaced string is ",str2)'''
str3=''
str2=re.finditer('\d',str1)
for x in str2:
    str3=str3+x.group()
print (str3)
import re

print ("Enter a alpha numeric string")

str1=input()
y=re.sub("\D+","",str1)
print (y)
"""
y=re.search("\d",x)
y.group()
3
y=re.search("\d+",x)
y.group()
3245
"""
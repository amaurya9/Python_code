import re
print ("plrase enter a string to manipulate ")
str1='ashok kokar okuoka'
#str2=re.match('ok',str1)
#print (str2.span())
#str3=re.search('ok',str1)
#print (str3.span())
#str4=re.subn('ok','OK',str1)
#print(str4)
#print(str1.split('ok'))
#print(re.findall('ok',str1))
str2=re.finditer('ok',str1)
for pattern in str2:
    print (pattern.span())

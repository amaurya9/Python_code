print ("Enter a sequence of whitespace separated words")

list1=input()
list2=[]
list3=[]
i=0
str1=""
#print (list2.append(str1))
for letter in list1:
    if letter == ' ' and str1 != "":
        list2.append(str1)
        str1=""
        #print (list2)
    elif letter == ' ' and str1 == "":
        pass
    else:
        str1+=letter
        #print (str1)
if str1 != "":
    list2.append(str1)
#print (list2)
while i < len(list2):
    if list2[i] in list3:
        pass
    else:
        list3.append(list2[i])
    i+=1

list3.sort()
print (list3)

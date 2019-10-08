str1=input ("Please enter a string ")
count=0
lenth=0
for letter in str1:
    if letter in ('A','E','I','O','U','a','e','i','o','u'):
        
        count = count + 1
        #print ("letter is ", letter)
    lenth=lenth+1
print ("number of vovels are",count)
print ("Length of string is ", lenth)

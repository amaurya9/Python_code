str1=input("Please Enter a string ")
y=0; z=0
for x in str1:
    if x in ("a","e","i","o","u","A","E","I","O","U"):
        y+=1
        #print ("Entered character is vowel")
    elif x in (" ","_","@","$",".","0","1","3","4","5","6","7","8","9"):
        pass
    else:
        z+=1
        #print (x)
print("Number of vowel is {} and consonant is {} in the given string {}".format(y,z,str1))
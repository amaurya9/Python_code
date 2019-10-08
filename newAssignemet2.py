"""Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3"""
import re
"""str1=input("please enter a sentence full with letters and digits")
str2=re.findall("[a-zA-Z]",str1)
print("Letters",len(str2))
str3=re.findall("\d",str1)
print("Digits",len(str3))"""


"""Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"""
"""str1=input("Please enter Alpha numerical string")
str2=re.findall("[a-z]",str1)
print("Lowercase:",len(str2))

str3=re.findall("[A-Z]",str1)
print("UpperCase:",len(str3))

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

value1=int(input("Please input digit to calculate"))
sum1=0
x=value1
for i in range(value1):
    sum1=sum1+x
    x=(x*10)+value1
    print(x)
print("sum of expression",sum1)"""

"""Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

sequence=input("please enter sequence of comma-separated numbers.")
list1=sequence.split(",")
print([x for x in list1 if int(x)%2!=0])
"""
"""
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
¡­
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
print("Please enter int for deposit or withdrawal")
totalAmount=0
while(True):
    str1=input()
    if not str1:
        break
    str2=str1.split(" ")
    if str2[0]=="D":
        totalAmount+=int(str2[1])
    elif str2[0]=="W":
        totalAmount-=int(str2[1])
    else:
        pass
print("total ammount is {}".format(totalAmount))
"""
"""A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
import re
str1=input("please input comma seprated password to validate")
str2=str1.split(",")

for password in str2:
    if re.search("[a-z]",password):
        pass
    else:
        continue
    if re.search("[0-9]",password):
        pass
    else:
        continue
    if re.search("[A-Z]",password):
        pass
    else:
        continue
    if re.search("[$#@]",password):
        pass
    else:
        continue
    if len(password)>=6 and len(password)<=12:
        pass
    else:
        continue
    print("valid password is: ",password)"""

"""You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

from operator import itemgetter

list1=[]
print("please enter string's containing name age and score")
while True:
    str1=input()
    if not str1:
        break
    list1.append(tuple(str1.split(",")))
list2=sorted(list1,key=itemgetter(0,1,2))
print(list2)"""

"""Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

"""

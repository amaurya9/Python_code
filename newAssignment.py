__author__ = 'amaurya'
"""list1=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        list1.append(i)
#list2=["12345","ashok","maurya"]
print(list1)
#print("," .join(list2))"""

#factorial

"""def fact(x):
    if type(x) is not int or x<0:
        return "not valid int"
    if x ==0:
        return 1
    return x*fact(x-1)
value=eval(input("please enter a int to calculate factorial"))
print(fact(value))"""

"""With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""

"""def dictionary(n):
    dict1={}
    for i in range(1,n+1):
        dict1[i]=i*i
    print(dict1)
x=eval(input("please enter a int for creation of dict"))
dictionary(x)"""

"""Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""

"""value=input("please enter comma seprated sequence of int")
l=value.split(",")
t=tuple(l)
print(l,t)"""

"""def list_tuple(n):
    list1=list()
    tuple1=tuple()
    for i in range(n):
        value=eval(input("please enter input value"))
        list1.append(value)
    tuple1=tuple(list1)
    print(list1,tuple1)
x=eval(input("please enter length of list or tupple"))
list_tuple(x)"""

"""Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

class Ashok:
    def __init__(self):
        self.str1=""
    def getString(self):
        self.str1=input("please enter a string")
        #return self.str1
    def printString(self):
        str2=self.str1.upper()
        print(str2)

if __name__ == '__main__':
    obj=Ashok()
    obj.getString()
    obj.printString()"""

"""
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
"""###import math

c=50
h=30
list1=[]
items=input("please enter comma seprated int value").split(",")

for d in items:
    x=int(round(math.sqrt((2*c*int(d))/h)))
    list1.append(str(x))
print(",".join(list1))
#print(list1)"""
"""
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

x=int(input("please enter x,y for creation of 2-dimentional arrey"))
y=int(input())
list1=[]
for i in range(x):
    list2=[]
    for j in range (y):
        list2.append(i*j)
    list1.append(list2)
    #print(list1)
print(list1)"""

"""Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world


str1=input("enter comma seprated list of string")
str2=str1.split(",")
print(str2)
items=[x for x in (input("please enter value").split(','))]
print(items)
#print(sorted(strings))
i=0;
#print(str2)
for i in range (int(len(str2)/2+1)):
    for j in range(1,len(str2)):
        if str2[j-1] >= str2[j]:
            copy=str2[j-1]
            print("value of j",j)
            #print(copy)
            str2[j-1]=str2[j]
            str2[j]=copy
        else:
            print("else part is executed")
        #print(str2)
    #print("value of i",i)
print(str2)
"""
"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
print("please enter sequence of lines")
list1=[]
while True:
    s=input()
    if s :
        list1.append(s.upper())
    else:
        break
for x in list1:
    print(x)
    """
"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

s=input("please enter white space seprated string ")
list1=[]
words=s.split(" ")
#print(words)
for x in words:
    if x not in list1:
        list1.append(x)
#print(list1)
print(" ".join(sorted(list1)))"""

"""Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

str1=input("please enter comma seprated 4 digit binary numbers")
list1=str1.split(",")
list2=[]
for x in list1:
    #print(int(x,2))
    if int(x,2)%5==0:
        list2.append(x)
print(",".join(list2))"""

"""Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
list1=[]
for i in range (1000,3001):
    str1=str(i)
    #print(str1[3])
    if int(str1[0])%2==0 and int(str1[1])%2==0 and int(str1[2])%2==0 and int(str1[3])%2==0:
            list1.append(str1)
print(",".join(list1))"""

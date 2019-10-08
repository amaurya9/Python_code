def IsOdd(number):
    return number & 1
#def IsEven (number):
 #   return number & 1

#number =int (input ("enter value"))
number =eval((input ("enter value")))#eval is a function which type cast the input to respective variable.
if IsOdd(number):
    print ("{} Number is odd".format(number))
else :
    print ("{} Number is even".format(number))
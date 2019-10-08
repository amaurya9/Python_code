def Sayhello (name):
    print ("hello " + name)
def details (age,education):
    print ("age is "+age+ " " +"Education is "+ education)
def MultipleValues():
    return 1,2,"hello"
#Sayhello(input ("Please enter your name"))
#details(input("enter your age "),input ("Enter your education"))
a,b,c=MultipleValues()
print ("return value is",a,b,c )
print ("A=%d B=%d C=%s "%(a,b,c)) #here it is % separated not comma separated
print ("a={} b={} c={}".format(a,b,c))#while using format you don't need to give type of the input
print ("a={2} b={0} c={1}".format(a,b,c))#we can print by using index in {} as well
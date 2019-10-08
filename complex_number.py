#!/usr/bin/python

class Complex:

    def __init__(self, real, img):
        self.real=real
        self.img=img
    def __del__(self):
        print("destructor is called")
    def __add__(self, c2):
        result=Complex(0,0)
        if(isinstance(c2,int)):
            result.real=self.real+c2
            result.img=self.img
        elif(isinstance(c2, Complex)):
            result.real=self.real+c2.real
            result.img=self.img+c2.img
        return result
    def __sub__(self, c2):
        result=Complex(0,0)
        if(isinstance(c2,int)):
            result.real=self.real-c2
            result.img=self.img
        elif(isinstance(c2, Complex)):
            result.real=self.real-c2.real
            result.img=self.img-c2.img
        return result
    def __mul__(self, c2):
        result=Complex(0,0)
        result.real=self.real*c2.real
        result.img=self.img*c2.img
        return result
    def __str__(self):
        """__str__: it is invoked when print statement is used to display the object. this method should return string form of the object."""
        return str(self.real)+"+"+str(self.img)+"i"
def Menu():
    choice =0
    print("1. Add 2 complex Numbers")
    print("2. Add integer to complex number")
    print("3. Subtract 2 complex number")
    print("4. subtract integer from complex number")
    print("5. Multiply an integer to complex number")
    print("6. Exit")
    choice=eval(input("enter your choice: "))
    return choice

def main():
    #help (complex)
    while True:
        choice =Menu()
        #x=Complex(0,0)
        if choice==1:
            r1,i1=eval(input("please enter real and imaginary part of complex number"))
            c1=Complex(r1,i1)
            r2,i2=eval(input("please enter real and imaginary part of second complex number"))
            c2=Complex(r2,i2)
            x=c1+c2
            print(x)
        elif choice ==2:
            r1,i1=eval(input("please enter real and imaginary part of complex number"))
            c1=Complex(r1,i1)
            c2=eval(input("please enter a int  number"))
            x=c1+c2
            print(x)
        elif choice == 6:
            break
        elif choice == 3:
            r1,i1=eval(input("please enter real and imaginary part of complex number"))
            c1=Complex(r1,i1)
            r2,i2=eval(input("please enter real and imaginary part of second complex number"))
            c2=Complex(r2,i2)
            x=c1-c2
            print(x)
        elif choice ==4:
            r1,i1=eval(input("please enter real and imaginary part of complex number"))
            c1=Complex(r1,i1)
            c2=eval(input("please enter a int number"))
            x=c1-c2
            print(x)
        elif choice == 5:
            r1,i1=eval(input("please enter real and imaginary part of complex number"))
            c1=Complex(r1,i1)
            r2,i2=eval(input("please enter real and imaginary part of second complex number"))
            c2=Complex(r2,i2)
            x=c1*c2
            print(x)
        else:
            print("please enter a number from menu")
            continue
if __name__=="__main__":
    main()

















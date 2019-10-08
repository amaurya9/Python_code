def menu():
    print("1 for ADD" "\n" "2 for SUB" "\n" "3 for multiplication" "\n" "4 for division" "\n" "5 for Exit")

    num= eval(input("select one option"))
    if num not in (1,2,3,4):
        return num,0,0
    else:
        print("Enter two value for arithmetic operation")
        num1=eval(input("Enter first value"))
        num2=eval(input("Enter second value"))
        return num,num1,num2
if __name__=="__main__":
    option= eval (input("please enter 0 for menu"))
    if option ==0:
        num,num1,num2=menu()
    else:
        print("not a valid number, please enter 0 for menu")
        num,num1,num2=menu()
    while True:

        if num ==1:
            sum=num1+num2
            print("Sum of value {} and {} is {}".format(num1,num2,sum))
            num,num1,num2=menu()
        elif num==2:
            sub=num1-num2
            print("Subtraction  of value {} and {} is {}".format(num1,num2,sub))
            num,num1,num2=menu()
        elif num==3:
            multi=num1*num2
            print("multiplication of value {} and {} is {}".format(num1,num2,multi))
            num,num1,num2=menu()
        elif num==4:
            div=num1/num2
            print("division  of value {} and {} is {}".format(num1,num2,div))
            num,num1,num2=menu()
        elif num==5:
            print("Exiting the program")
            break
        else:
            print("not a valid option, please select one menu option")
            num,num1,num2=menu()
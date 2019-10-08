print ("Please inter upper and lower bound for prim number")
num1=eval(input("enter lower range for prim number"))
num2=eval(input("enter upper value"))
print("prime number between range {} and {} is ".format(num1,num2))
for x in range (num1,num2):
    for y in range (2,x):
        if x%y==0:
            break
        if y==x-1:
            print("{} ".format(x))



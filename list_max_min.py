length=eval(input("please enter length of list"))
print("Enter the element of list")
list=[]
for x in range(length):
    list.append(eval(input("Enter element")))
list.sort()
print("min value of list is {} and max is {}".format(list[0],list[length-1]))
#add value in a+aa+aaa+.....+till a manner.
def main():
    input_value=eval(input("please enter value to perform operation"))
    x=input_value
    sum_value=input_value
    for y in range (1,input_value):
        #print(sum_value)
        x=x*10+input_value
        sum_value+=x
        #print(sum_value)
    print("Sum of all value is {}".format(sum_value))

if __name__ == '__main__':
    main()
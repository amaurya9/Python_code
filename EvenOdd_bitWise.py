def main():
    print("Enter a number to identify if its a even or odd number")
    x=eval(input())
    if (x | 1)==x:
        print("Entered value {} is odd".format(x))
    elif x ==0:
        print("Zero is neither even nor odd")
    else:
        print("Entered value {} is Even".format(x))
if __name__=="__main__":
    main()
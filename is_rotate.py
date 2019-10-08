def ISRotateString(string1,string2):
    string1+=string1
    return string2 in string1
if __name__=="__main__":
    string1=input("Enter Input string")
    string2=input("Enter string to be checked as rotation or not")
    if ISRotateString(string1,string2):
        print("{} is a rotation of {}".format(string1,string2))
    else:
        print("{} is not a rotation of {}".format(string1,string2))

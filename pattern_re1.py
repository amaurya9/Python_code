#!/usr/bin/python
import re
def main():
    fd = open("1.txt")
    data = fd.read()
    print (data)
    print("pattern is :-------")
    #print(re.findall("a|b",data))
    #print( re.findall("a[ab]+",data))
    #print( re.findall("a[ab]+?",data))
    #print( re.findall("\w+",data))
    #print( re.findall("[a-z]+",data))
    #print( re.findall("[A-Z]+",data))
    #print( re.findall("[a-zA-Z]+",data))
    #print( re.findall("[A-Z][a-z]+",data))
    #print( re.findall("[A-Z][a-z]",data))
    print( re.findall("a\w+",data))
    print( re.findall("b\w",data))
    print( re.findall("a\w+b",data))

if __name__ == "__main__":
    main()
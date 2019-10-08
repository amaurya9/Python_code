def main():
    x=str (input("Please Enter a String "))
    y=0;z=0
    for i in x:
        if i in ("A","E","I","O","U","a","e","i","o","u"):
            y+=1
        elif i in (" ","@","$",".","_"):
            pass
        else:
            z+=1
    print("Number of vowels and Consonants in String is {}, {}".format(y,z))
if __name__ == '__main__':
    main()
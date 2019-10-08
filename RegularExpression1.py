import re

if __name__ == '__main__':
    #fd=open("audio.conf")
#    file=eval(input("please enter pattern to search in given audio.conf file"))
 #   replace=eval(input("please enter value to replace the pattern and num to be updated"))
  #  num=eval(input())
   # for line in fd:
        #print(line)
        #print(file)
        #if re.search("HFP",line):
            #print(line)
            #line=re.sub("st","at",line)
            #print("entered file exist at beginning of line")
            #line,x=re.subn("to","maurya",line)
            #print(line,x)
            #line=re.split("HFP",line,1)
            #print(line)
            #line=re.findall("HFP",line)
            #print(line)
            #line=re.finditer("HFP",line)
            #x=re.findall(r"([A-Z]+)",line)
            #print(x)
            #print("number of matched RE in string")
            #print (len(x))
            #iter1=re.finditer(r"([A-Z]+)",line)
            #for match in iter1:
             #   print(match.group())
              #  print(match.span())
               # print(match.start())
                #print(match.end())
        #print(re.sub("[a-zA-Z]+","",line))
        #matched=re.findall("[^a-zA-Z]+",line)
        #print(matched)
        """if re.match("#",line):
            pass
        else:
            print(line)"""
        """if re.search("(\w+)@([a-z]+).(com|org|edu|in|nic)",line):
            x=re.search("(\w+)@([a-z]+).(com|org|edu|in|nic)",line)
            print(line)
            x.group()
            x.groups()"""
        #x = re.match( "(bh(at(ta))d)", "bhattad.jeetendra@gmail.com")
        #x.groups(0)
        #else:
           # print("not a valid email address")
        #print(re.findall("\w+",line))
        #if re.match("#",line):
         #   print(line)
        #list1=re.split(" ",line)
        #print(list1,len(list1))
        #if re.sub(file,replace,line,num):
         #   print(re.sub(file,replace,line,num))
        #print(line)
        #if re.search("\Zany",line):
         #   print(line)
          #  print("Entered pattern is present at the end of the line")
        #if line.endswith("any"):
            #print(line)
        #else:
         #   print("not entered in if")
ip1=eval(input("please enter ip address"))
if re.match("172.",ip1):
    print("entered value is of internet range")
elif(re.match("10.",ip1)):
    print("Entered IP is of range intranet")
else:
    print("ip is not range of internet or intranet")
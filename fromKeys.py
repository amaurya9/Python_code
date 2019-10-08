def compareDict(dict1,dict2):
    if len(dict1)!=len(dict2):
        return False
    for  keys in dict1:
        if keys in dict2:
            #print(keys, dict1[keys], dict2[keys])
            if dict1[keys]==dict2[keys]:
                continue
            else:
                return False
        else:
            return False
            #break
    return True
def fromkeys1(teacher,tupp1):
    if not isinstance(teacher,dict):#used for validating if teacher is of dict type ot any value of respective type
        return False
    if not isinstance(tupp1,tuple) and not isinstance(tupp1,list):
        print(type(tupp1))
        for key in teacher:
            teacher[key]=tupp1
    else:
        i=0
        #print()
        for key in teacher:
            if i< len(teacher):
                teacher[key]=tupp1[i]
                i+=1
            else:
                teacher[key]=None
    return teacher
def main():
    print("please Enter keys and value to generate a dict or type 0 for closure")
    dict1={}
    while(True):
        x=eval(input())
        if x==0:
            break
        else:
            dict1[x]=input()
    return dict1
if __name__ == '__main__':
    #main()
    teacher=main()
    teache3=main()
    teacher2=fromkeys1(teacher,("akash","25","magarpatta city"))
    print(compareDict(teacher,teache3))
    print(teacher2)
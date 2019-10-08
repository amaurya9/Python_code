import collections

#do all dict program using this
#check for defaultdict
#bite array
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


if __name__ == '__main__':
    #main()
    teacher={"name":"Ashok","age":"27","Address":"Yerwada"}
    #teache3=main()
    teacher2=fromkeys1(teacher,("akash","25","magarpatta city"))
#    print(compareDict(teacher,teache3))
    #teacher2=collections.
    print(teacher2)
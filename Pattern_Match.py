import re
def TestPatterns(test, patterns=[]):
    #look for each pattern in test and print the result
    for pattern in patterns :
        print ('matching {}'.format(pattern))
        for match in re.finditer(pattern,test):
            s=match.start()
            e=match.end()
            print('{0}:{1}) string ={2}'.format(s, e - 1, test[s:e]))
    return
if __name__=='__main__':
    #TestPatterns('abbaaabbbbaaaaa',['ab','ab*','ab+','ab?','ab{3}','ab{2,3}'])
    #TestPatterns('abbaaabbbbaaaaa',['[ab]','a[ab]+','a[ab]+?'])
    TestPatterns('This is Qlogic --python.training',['[^ .-]+','[a-z]+','[A-Z]+','[a-zA-Z]+','[a-z][A-Z]+',"[A-Z][a-z]+",'[a][g]+'])
    #TestPatterns('This is Qlogic --python.training',['a.','b.','a.*b','a.*?b'])
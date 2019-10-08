def isSuperSet(arrA,arrB):
    hash = {}
    for x in arrA:
        if x not in hash:
            hash[x] = 0
        hash[x] += 1
    for x in arrB:
        if x not in hash or hash[x] == 0:
            return False
        hash[x] -= 1
    return True
arrA="Hello World"
arrB = "Worldols"

if isSuperSet(arrA,arrB):
    print("is a Super set")
else:
    print("Not a super set")
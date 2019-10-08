#!/usr/bin/python

class Molecule:
    # constructor
    def __init__(self, symbol, atomic_weight):
        print("Constructor")
        self.symbol = symbol
        self.atomic_weight = atomic_weight
        print(id(self.symbol))
    # destructor
    def __del__(self):
        print("Destructor")
    # getitem method making object accessible using index like an array
    def __getitem__(self, index):
        print("GetItem invoked index = %d"%index)
    # setitem method making object mutable using index like an array
    def __setitem__(self, index, value):
        print("SetItem invoked index = %d"%index)
    # getslice to make object accessible using slicing syntax
    def __getslice__(self, start, end = 10, step = 1):
        print("start = %d end = %d step = %d"%(start, end, step))
    # call to make object callable like function
    def __call__(self, *args):
        print("Using object like function {}".format(args))
    # arithmetic operations
    def __add__(self, obj):
        print("Adding 2 objects")
    
    def __sub__(self, obj):
        print("Subtracting 2 objects")
    
    def __mul__(self, obj):
        print("Multiple 2 objects")
    
    def __div__(self, obj):
        print("Division 2 objects")
    # relational operations
    def __cmp__(self, obj):
        print("Compare 2 objects")
        return 0

if __name__ == "__main__":
    m = Molecule("W", 83)
    m[2]
    m[2] = 3
    m[1:2]
    m(1,2,3)
    m+10
    m-10
    m*10
    m/10
    m == m
    x = getattr(m, "symbol")
    print (x, id(x))
    print(hasattr(m,"symbol"))

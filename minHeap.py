from heapq import heappop, heappush,heapify

class Heap:
    def __init__(self):
        self.heap = []

    def insert(self,k):
        return heappush(self.heap,k)

    def remove(self):
        return heappop(self.heap)

    def getMin(self):
        return self.heap[0]

if __name__ == "__main__":
    heapObj = Heap()
    heapObj.insert(3)
    heapObj.insert(2)
    heapObj.insert(1)
    heapObj.insert(15)
    heapObj.insert(5)
    heapObj.insert(4)
    heapObj.insert(2)
    heapObj.insert(45)

    #print(heapObj.getMin())
    #print(heapObj.remove())
    print(heapObj.heap)
    print(heapObj.remove())
    print(heapObj.remove())
    #print(heapObj.heap)
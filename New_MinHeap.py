class MinHeap:
    def __init__(self,items = []):
        self.heap = []
        for x in items:
            self.heap.append(x)
            self._pushUp(len(self.heap)-1)

    def push_min(self,element):
        self.heap.append(element)
        self._pushUp(len(self.heap)-1)

    def _pushUp(self,i):
        root = (i-1)//2
        if root < 0:
            return
        if self.heap[root] >= self.heap[i]:
            self.heap[root],self.heap[i] = self.heap[i],self.heap[root]
            self._pushUp(root)

    def pop_min(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        elif len(self.heap) > 1:
            self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]
            min = self.heap.pop()
            self._floatDown(0)
            return min
        else:
             print("list is empty")

    def _floatDown(self,i):
        left = i*2 + 1
        right = i*2 +2
        heap = self.heap

        if len(heap) > left:
            if len(heap) > right and heap[right] <= heap[i] and heap[right] < heap[left]:
                heap[i],heap[right] = heap[right],heap[i]
                self._floatDown(right)
            elif heap[left] <= heap[i]:
                heap[i], heap[left] = heap[left], heap[i]
                self._floatDown(left)
            else:
                return
        elif len(heap) > right:
            heap[i], heap[right] = heap[right], heap[i]
            self._floatDown(right)
        else:
            return

if __name__ == "__main__":
    mheap= MinHeap([15,12,15])
    mheap.push_min(95)
    mheap.push_min(3)
    mheap.push_min(21)
    mheap.push_min(10)
    print(mheap.heap)
    print(mheap.pop_min())
    print(mheap.pop_min())
    print(mheap.heap)
    print(mheap.pop_min())
    print(mheap.pop_min())
    print(mheap.pop_min())

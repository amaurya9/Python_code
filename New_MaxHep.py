class MaxHeap:
    def __init__(self,items=[]):
        self.heap = []
        for x in items:
            self.push_max(x)

    def push_max(self,element):
        self.heap.append(element)
        self._pushUp(len(self.heap)-1)
        return self.heap

    def _pushUp(self,i):
        if i == 0:
            return
        root = (i-1)//2
        if self.heap[root] < self.heap[i]:
            self.heap[root],self.heap[i] = self.heap[i],self.heap[root]
            self._pushUp(root)
        return

    def pop_max(self):
        heap = self.heap
        if len(heap) > 1:
            heap[0],heap[-1] = heap[-1],heap[0]
            max = heap.pop()
            self._bubble_down(0)
            return max
        elif len(heap) == 1:
            return heap.pop()
        else:
            print("list is empty")


    def _bubble_down(self,i):
        heap = self.heap
        left = (2*i + 1)
        right = (2*i + 2)
        if left < len(heap):
            if right < len(heap) and heap[right] >= heap[i] and heap[right] > heap[left]:
                heap[right],heap[i] = heap[i],heap[right]
                self._bubble_down(right)
            elif heap[left] >= heap[i]:
                heap[left],heap[i] = heap[i],heap[left]
                self._bubble_down(left)
            else:
                return
        elif right < len(heap) and heap[right] >= heap[i]:
            heap[right],heap[i] = heap[i],heap[right]
            self._bubble_down(right)
        else:
            return

if __name__ == "__main__":
    mheap= MaxHeap([15,12,15])
    mheap.push_max(95)
    mheap.push_max(3)
    mheap.push_max(21)
    mheap.push_max(10)
    print(mheap.heap)
    print(mheap.pop_max())
    print(mheap.pop_max())
    print(mheap.heap)
    print(mheap.pop_max())
    print(mheap.pop_max())
    print(mheap.pop_max())

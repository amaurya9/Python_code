class Heap:
    def __init__(self,items=[]):
        self.heap = []
        for item in items:
            self.heap.append(item)
            self._pushUp(len(self.heap)-1)

    def push_min (self,item):
        self.heap.append(item)
        self._pushUp(len(self.heap) - 1)

    def _pushUp(self,index):
        root = (index-1)//2
        if root < 0:
            return
        if self.heap[root] > self.heap[index]:
            self.heap[root],self.heap[index] = self.heap[index],self.heap[root]
            self._pushUp(root)
        else:
            return self.heap

    def pop_min(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        elif len(self.heap) > 1:
            self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]
            max = self.heap.pop()
            self.bubbleDown(self.heap,0)
            return max
        else:
            return "heap is empty"

    def bubbleDown(self,heap,index):
        left = 2*index +1
        right = 2*index +2
        smallest = index

        if right < len(heap) and heap[left] < heap[smallest] and heap[right] < heap[left]:
            smallest = right
        elif left < len(heap) and heap[left] < heap[smallest]:
            smallest = left

        if smallest != index:
            heap[index],heap[smallest] = heap[smallest],heap[index]
            self.bubbleDown(heap,smallest)
        return

if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    heap = Heap(array)
    heap.push_min(3)
    heap.push_min(9)
    print(heap.heap)
    print(heap.pop_min())
    print(heap.pop_min())
    print(heap.pop_min())
    print(heap.pop_min())
    print(heap.pop_min())
    print(heap.pop_min())
    print(heap.pop_min())
    print(heap.pop_min())
    print(heap.pop_min())
    print(heap.pop_min())
    print(heap.pop_min())
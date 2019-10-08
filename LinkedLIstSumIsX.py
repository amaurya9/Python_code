class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = Node(data)

    def countPair(self,root1,root2,x):
        if root1 is None or root2 is None:
            return 0
        hash = set()
        count = 0
        while root2:
            hash.add(root2.data)
            root2 = root2.next
        while root1:
            y = x - (root1.data)
            if y in hash:
                count += 1
            root1 = root1.next
        return count

if __name__ == "__main__":
    llist1 = LinkedList()
    llist2 = LinkedList()
    list1 = [1,2,3,4,5,6]
    list2 = [11,12,13]
    for data in list1:
        llist1.insert(data)
    for data in list2:
        llist2.insert(data)
    x = 16
    print(llist1.countPair(llist1.head,llist2.head,x))
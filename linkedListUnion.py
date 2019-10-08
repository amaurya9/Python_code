class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            root = self.head
            while (root.next):
                root = root.next
            root.next = Node(data)
    def print(self):
        root = self.head
        while(root):
            print(root.data,end=" ")
            root = root.next
        print()

    def unionLinkedList(self,root):
        tmp1 = self.head
        tmp2 = root
        unionList = set()
        while tmp1:
            unionList.add(tmp1.data)
            tmp1 = tmp1.next
        while tmp2:
            unionList.add(tmp2.data)
            tmp2 = tmp2.next
        return unionList

    def addOneToLinkedList(self):
        root = self.head
        print(self.head.data)
        carry = 0
        carry = self.addOneUtil(root,carry)
        if carry == 1:
            node = Node(carry)
            node.next = self.head
            self.head = node


    def addOneUtil(self,root,carry):
        if root is None:
            return 0
        carry = self.addOneUtil(root.next,carry)
        if root.next is None or carry == 1:
            if root.data is 9:
                root.data = 0
                carry = 1
            else:
                root.data += 1
                carry = 0
            #return carry

        return carry

if __name__ == "__main__":
    str1 = [9,9,9,9,9,9]
    #print(set(str1))
    str2 = [1,2,8,6,2]
    llist1 = LinkedList()
    llist2 = LinkedList()
    llist3 = LinkedList()
    for x in str1:
        llist1.insert(x)
    for x in str2:
        llist2.insert(x)
    list = llist1.unionLinkedList(llist2.head)
    for x in list:
        llist3.insert(x)
    #llist3.print()
    llist1.addOneToLinkedList()
    llist1.print()



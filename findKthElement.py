class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    def findKthElement(self, root, k):
        if root is None or k[0] < 0:
            return
        self.findKthElement(root.left,k)
        print(root.data, k, end=",")
        if k[0]==0:
            print("kth element is:",root.data)
            k[0] -= 1
        else:
            k[0] -= 1
        self.findKthElement(root.right,k)

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)

    def _insert(self,curr_node,data):
        if curr_node.data > data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(curr_node.left,data)
        if curr_node.data < data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(curr_node.right,data)

if __name__ == "__main__":
    bst = BST()
    x = [1, 5, 4, -6, 3, 0, 6, 7, -1, -4, -5]
    for i in x:
        bst.insert(i)
    k = [5]
    
    if len(x) < k[0]:
        print("K is out of range ")
    bst.findKthElement(bst.root,k)
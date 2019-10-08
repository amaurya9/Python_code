class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self,curr_node, data):
        if curr_node.data > data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(curr_node.left, data)
        elif curr_node.data < data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(curr_node.right, data)
        else:
            print("element already exist ass part of BST")

    def printMin(self):
        if self.root is None:
            print(-1)
        else:
            curr_node = self.root
            while curr_node is not None:
                backup = curr_node.data
                curr_node = curr_node.left
            print(backup)


if __name__ == "__main__":
    bst = BST()
    x = [1, 5, 4, -6, 3, 0, 6, 7, -1, -4, -5]
    for i in x:
        bst.insert(i)
    print("minimum value in list is :", end=" ")
    bst.printMin()


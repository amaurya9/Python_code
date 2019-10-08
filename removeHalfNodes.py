class Node:
    def __init__(self,data):
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

    def _insert(self,curr_node,data):
        if curr_node.data > data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(curr_node.left,data)
        elif curr_node.data < data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(curr_node.right,data)
        else:
            print("Already have a Node with same value")

    def removeHalfNodes(self, curr_node):
        if curr_node is None:
            return curr_node
        curr_node.left = self.removeHalfNodes(curr_node.left)
        if curr_node.left is None and curr_node.right is None:
            print(f"curr data {curr_node.data}")
            return curr_node
        elif curr_node.right is None:
            curr_node = curr_node.left
            return curr_node
        elif curr_node.left is None:
            curr_node = curr_node.right
            return curr_node
        print("crossed left")
        curr_node.right = self.removeHalfNodes(curr_node.right)
        return curr_node

    def inorderTraversal(self,curr_node):
        if curr_node is None:
            return
        else:
            self.inorderTraversal(curr_node.left)
            print(curr_node.data, end = " ")
            self.inorderTraversal(curr_node.right)

    def minRight(self,curr_node):
        while (curr_node.left is not None):
            curr_node = curr_node.left
        return curr_node.data

    def deleteNode(self,curr_node, data):
        if curr_node is None:
            return None
        if curr_node.data > data:
            curr_node.left = self.deleteNode(curr_node.left, data)
        elif curr_node.data < data:
            curr_node.right = self.deleteNode(curr_node.right, data)
        else:
            if curr_node.left is None and curr_node.right is None:
                curr_node = None
            elif curr_node.left is None:
                curr_node = curr_node.right
            elif curr_node.right is None:
                curr_node = curr_node.left
            else:
                curr_node.data = self.minRight(curr_node.right)
                curr_node.right = self.deleteNode(curr_node.right, curr_node.data)
        return curr_node

    def inorderSucssesor(self,curr_node,data):
        if curr_node is None:
            return curr_node
        while curr_node.data != data:
            if curr_node.data > data:
                s = curr_node.data
                curr_node = curr_node.left
            elif curr_node.data < data:
                curr_node = curr_node.right
        else:
            if curr_node.right is not None:
                curr_node = curr_node.right
                while curr_node.left is not None:
                    curr_node = curr_node.left
                return curr_node.data
        return s


if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(12)
    bst.insert(14)
    bst.insert(11)
    bst.insert(6)
    bst.insert(4)
    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    bst.insert(7)
    print("new BST with no single Node is :")
    #bst.removeHalfNodes(bst.root)
    #bst.inorderTraversal(bst.root)
    print(bst.inorderSucssesor(bst.root,10))
    """bst.deleteNode(bst.root,6)
    print()
    bst.inorderTraversal(bst.root)
    bst.deleteNode(bst.root, 4)
    print()
    bst.inorderTraversal(bst.root)
    bst.deleteNode(bst.root, 2)
    print()
    bst.inorderTraversal(bst.root)"""

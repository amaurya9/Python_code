class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)

    def _insert(self,curr_node,data):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(curr_node.left,data)
        elif(data > curr_node.data):
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(curr_node.right,data)
        else:
            print("data already exist in BST")

    def leftSideTraversal(self, curr_node):
        if curr_node is None:
            return
        elif(curr_node.left is None) and curr_node.right is None:
            return
        else:
            print(curr_node.data, end= " ")
            self.leftSideTraversal(curr_node.left)

    def childItemTraversal(self, curr_node):
        if curr_node is None:
            return
        elif(curr_node.left is None) and curr_node.right is None:

            print(curr_node.data, end= " ")

        else:
            self.childItemTraversal(curr_node.left)
            self.childItemTraversal(curr_node.right)

    def rightSideTraversalInReverse(self,curr_node):
        if curr_node is None:
            return
        elif (curr_node.left is None) and (curr_node.right is None):
            return
        else:
            self.rightSideTraversalInReverse(curr_node.right)
            print(curr_node.data, end= " ")

    def boundaryTraversal(self):
        self.leftSideTraversal(self.root)
        self.childItemTraversal(self.root)
        self.rightSideTraversalInReverse(self.root.right)
        print()

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
    print("Boundary level traversal of the Tree is : ")
    bst.boundaryTraversal()

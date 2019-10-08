class Node:
    def __init__(self,data = None):
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
            self._insert(data,self.root)

    def _insert(self,data,curr_node):
        if data < curr_node.data:
            if curr_node.left is not None:
                self._insert(data,curr_node.left)
            else:
                curr_node.left = Node(data)
        elif data > curr_node.data:
            if curr_node.right is not None:
                self._insert(data,curr_node.right)
            else:
                curr_node.right = Node(data)
        else:
            print("Value already exist")

    def find(self, data):
        if self.root is None:
            return None
        else:
            is_available = self._find(self.root, data)
            if is_available:
                return is_available
            return None

    def _find(self, curr_node, data):
        if curr_node.data < data:
            if curr_node.right is not None:
                y = self._find(curr_node.right, data)
                return y

        elif curr_node.data > data:
            if curr_node.left is not None:
                x = self._find(curr_node.left, data)
                return x
        else:
            return True
        return None

    def inorderItrative(self):
        if self.root:
            stack = []
            curr_node = self.root
            print("Inorder traversal using Iterative method:")
            while curr_node is not None or len(stack) > 0:
                if curr_node is not None:
                    stack.append(curr_node)
                    curr_node = curr_node.left
                else:
                    curr_node = stack.pop()
                    print(curr_node.data, end=" ")
                    curr_node = curr_node.right
            print()

    def preorderIterative(self):
        if self.root:
            stack = []
            curr_node = self.root
            print("preorder traversal using iterative method:")
            while curr_node is not None or len(stack) > 0:

                if curr_node is not None:
                    print(curr_node.data, end=" ")
                    stack.append(curr_node)
                    curr_node = curr_node.left
                else:
                    curr_node = stack.pop()
                    curr_node = curr_node.right
            print()

    def postorderIterative(self):
        if self.root:
            stack1 = []
            stack2 = []
            curr_node = self.root
            print("PostOder traversal using iterative method:")
            while curr_node is not None or len(stack1) > 0:
                if curr_node is not None:
                    stack2.append(curr_node.data)
                    stack1.append(curr_node)
                    curr_node = curr_node.right
                else:
                    curr_node = stack1.pop()
                    curr_node = curr_node.left
            print(*stack2[::-1])


if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(12)
    bst.insert(14)
    bst.insert(11)
    bst.insert(6)
    bst.insert(4)
    bst.insert(5)
    bst.insert(7)
    #print(bst.root.data)
    #print(bst.find(11))
    #print(bst.find(15))
    bst.inorderItrative()
    bst.preorderIterative()
    bst.postorderIterative()

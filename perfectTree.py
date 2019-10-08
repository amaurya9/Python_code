class Node:
    def __init__(self,data):
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
            self._insert(self.root, data)

    def _insert(self, curr_node, data):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(curr_node.left, data)
        elif (data > curr_node.data):
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(curr_node.right, data)
        else:
            print("data already exist in BST")

    def depthTree(self):
        if self.root is None:
            return 0
        else:
            curr_node = self.root
            d = 0
            while curr_node.left is not None:
                curr_node = curr_node.left
                d += 1
            return d

    def perfectTree(self, curr_node, d, level=0):
        if curr_node is None:
            return True
        if curr_node.left is None and curr_node.right is None:
            print("level", level)
            return d == level
        if curr_node.left is None or curr_node.right is None:
            print("level for false", level)
            return False
        if self.perfectTree(curr_node.left,d,level + 1) and self.perfectTree(curr_node.right,d,level + 1):
            return True
        return False

    def fullTree(self,curr_node):
        if curr_node is None:
            return True
        if curr_node.left is None or curr_node.right is None:
            return False

        if self.fullTree(curr_node.left) and self.fullTree(curr_node.right):
            return True
        return False

    def identical(self,curr_node,second_node):
        if curr_node is None and second_node is None:
            return 1
        if curr_node is None or second_node is None:
            return 0
        if curr_node.data != second_node.data:
            return 0
        if self.identical(curr_node.left, second_node.left) and self.identical(curr_node.right, second_node.right):
            return 1
        return 0

    def subTree(self, curr_node, second_node):
        if second_node is None:
            return 1
        if curr_node is None:
            return 0
        if self.identical(curr_node,second_node):
            return 1
        if self.subTree(curr_node.left,second_node) or self.subTree(curr_node.right,second_node):
            return 1
        return 0


    def ancestorNode(self,curr_node,node):
        if curr_node is None:
            return False
        if curr_node.data == node:
            return True
        if self.ancestorNode(curr_node.left,node) or self.ancestorNode(curr_node.right,node):
            print(curr_node.data, end=" ")
            return True
        return False

    def lcaNode(self, curr_node, node1, node2):
        if curr_node is None:
            return None
        if curr_node.data == node1 or curr_node.data == node2:
            return curr_node
        left = self.lcaNode(curr_node.left, node1, node2)
        right = self.lcaNode(curr_node.right, node1, node2)

        if left and right:
            return curr_node
        else:
            return left or right

    def nodeKdistance(self,curr_node,k):
        if curr_node is None:
            return None
        if k == 0:
            print(curr_node.data, end = " ")
        else:
            self.nodeKdistance(curr_node.left,k-1)
            self.nodeKdistance(curr_node.right,k-1)



if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(12)
    bst.insert(14)
    bst.insert(11)
    bst.insert(6)
    bst.insert(8)
    bst.insert(5)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    #d = bst.depthTree()
    #print (d)
    #if (bst.perfectTree(bst.root,d)):
    #    print("given tree is a perfect tree")
    #else:
    #    print("Not a perfect Tree")

    bst.ancestorNode(bst.root,3)
    #curr_node = bst.lcaNode(bst.root, 5, 11)
    #print(f"lowest common ancestor is {curr_node.data}")
    #bst.nodeKdistance(bst.root,1)

    bst1 = BST()
    bst1.insert(6)
    bst1.insert(8)
    bst1.insert(5)
    bst1.insert(7)
    bst1.insert(4)
    bst1.insert(2)
    #if bst.subTree(bst.root,bst1.root):
    #    print("given tree is subtree of first tree")
    #else:
    #    print("subtree is not part of tree")
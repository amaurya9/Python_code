class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class MinMax:
    def __init__(self,data):
        self.isBST = True
        self.size = 1
        self.min = data
        self.max = data

def sizOfBST(curr_node):
    if curr_node is None:
        return 0
    if curr_node.left is None and curr_node.right is None:
        return MinMax(curr_node.data)
    if curr_node.left is None :
        minMax = MinMax(curr_node.data)
        minMax.size = 0
        return minMax
    if curr_node.right is None:
        minMax = MinMax(curr_node.data)
        minMax.size = 0
        return minMax

    leftMinMax = sizOfBST(curr_node.left)
    rightMinMax = sizOfBST(curr_node.right)

    if (leftMinMax.isBST and rightMinMax.isBST) and (curr_node.data >= leftMinMax.min and curr_node.data <= rightMinMax.max):
        leftMinMax.size = leftMinMax.size + rightMinMax.size + 1
        leftMinMax.max = rightMinMax.max

        print(curr_node.data,leftMinMax.size,leftMinMax.min,leftMinMax.max)
        return leftMinMax
    else:
        leftMinMax.size = max(leftMinMax.size, rightMinMax.size)
        leftMinMax.isBST = False
        print("else part",curr_node.data, leftMinMax.size, leftMinMax.min, leftMinMax.max)
        return leftMinMax

if __name__ == "__main__":
    tree = Node(25)
    tree.left = Node(18)
    tree.left.left = Node(19)
    tree.left.left.right = Node(15)
    tree.left.right = Node(20)
    tree.left.right.left = Node(18)
    tree.left.right.right = Node(25)
    tree.right = Node(50)
    tree.right.left = Node(35)
    tree.right.left.left = Node(20)
    tree.right.left.left.right = Node(25)
    tree.right.left.right = Node(40)
    tree.right.right = Node(60)
    tree.right.right.left = Node(55)
    tree.right.right.right = Node(70)
    maxSize = sizOfBST(tree)
    print("max size of a BST in tree is:",maxSize.size)
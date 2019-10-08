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
            self._insert(self.root,data)

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
            print("element already exist in tree")

    def height_bst(self,curr_node):
        if curr_node is None:
            return 0
        else:
            lh = self.height_bst(curr_node.left)
            rh = self.height_bst(curr_node.right)
            return (max(lh, rh) + 1)

    def sum_tree(self,curr_node):
        if curr_node is None:
            return 0
        else:
            lsum = self.sum_tree(curr_node.left)
            rsum = self.sum_tree(curr_node.right)
            return lsum + rsum + curr_node.data

    def tree_sum_iterative(self):
        curr_node = self.root
        stack = []
        sum1 = 0
        while curr_node is not None or len(stack) > 0 :
            if curr_node is not None:
                sum1 = sum1 + curr_node.data
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop()
                curr_node = curr_node.right
        return sum1

    def leaf_node(self):
        curr_node = self.root
        stack = []
        count = 0
        while curr_node is not None or len(stack) > 0:
            if curr_node is not None:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop()
                if curr_node.left is None and curr_node.right is None:
                    count += 1
                curr_node = curr_node.right
        return count


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

    print(f"height of tree is {bst.height_bst(bst.root)}")
    print(f"sum of the tree is : {bst.sum_tree(bst.root)}")
    print("sum is:", bst.tree_sum_iterative())
    print(f"number of leaf node is: {bst.leaf_node()}")

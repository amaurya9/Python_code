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
            self._insert(self.root,data)

    def _insert(self,curr_node,data):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(curr_node.left,data)
        elif data > curr_node.data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(curr_node.right,data)
        else:
            print("node already exist in BST")

    def diagonalOrderTraversal(self):
        if self.root is None:
            return
        queue = []
        dict_dist = {}
        dict_data = {}
        queue.append(self.root)
        dict_dist[self.root] = 0
        while queue:
            curr_node = queue.pop(0)
            if curr_node.left is not None:
                queue.append(curr_node.left)
                dict_dist[curr_node.left] = dict_dist[curr_node] + 1
            if curr_node.right is not None:
                queue.append(curr_node.right)
                dict_dist[curr_node.right] = dict_dist[curr_node]

            dist = dict_dist[curr_node]
            if dict_data.get(dist) is None:
                dict_data[dist] = []
            dict_data[dist].append(curr_node.data)
        for x in dict_data.values():
            print(*x)

    def removeHalfNode(self,curr_node):
        if curr_node is None:
            return None
        if curr_node.left is None and curr_node.right is None:
            return curr_node
        curr_node.left = self.removeHalfNode(curr_node.left)
        curr_node.right = self.removeHalfNode(curr_node.right)

        if curr_node.left is None:
            print("left is none and value of right is ",curr_node.right.data)
            return curr_node.right
        elif curr_node.right is None:
            print("right is none and value of left is ", curr_node.left.data)
            return curr_node.left
        else:
            print("fall in else",curr_node.data)
            return curr_node

    def inorderTraversal(self,curr_node):
        if curr_node is None:
            return
        self.inorderTraversal(curr_node.left)
        print(curr_node.data,end=" ")
        self.inorderTraversal(curr_node.right)

    """def maxPathSum(self,curr_node):
        if curr_node is None:
            return [0,[]]

        lh = self.height(curr_node.left)
        rh = self.height(curr_node.right)
        pd = [0,[]]
        pd[0] = lh[0]+rh[0]+curr_node.data
        pd[1] = pd[1] + lh[1] + [curr_node.data] + rh[1]
        #print("****************lh and rh", lh, rh, pd)
        sumL = self.maxPathSum(curr_node.left)
        sumR = self.maxPathSum(curr_node.right)
        #print("****************sumL,sumR", sumL,sumR)
        maxSum = max(sumL,sumR)

        return max(pd,maxSum)

    def height(self,curr_node):
        if curr_node is None:
            return [0,[]]
        lh = self.height(curr_node.left)
        rh = self.height(curr_node.right)
        #print("lh and rh",lh,rh,curr_node.data)
        max_data = max(lh,rh)
        max_data[0] += 1
        max_data[1].append(curr_node.data)
        #print(max_data)
        return max_data
"""
if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(12)
    bst.insert(14)
    bst.insert(11)
    bst.insert(6)
    bst.insert(4)
    bst.insert(-7)
    bst.insert(-13)
    bst.insert(2)
    bst.insert(7)
    #print(f"Diagonal View of the Tree is : ")
    #bst.diagonalOrderTraversal()
    #bst.inorderTraversal(bst.root)
    #print("\nTree after removal of half nodes")
    #bst.removeHalfNode(bst.root)
    #bst.inorderTraversal(bst.root)
    print(bst.maxPathSum(bst.root))
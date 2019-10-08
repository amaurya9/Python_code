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
            print("node already exist in tree")

    def maxPathSum(self, curr_node, maxSum):
        if curr_node is None:
            return 0
        if curr_node.left is None and curr_node.right is None:
            return curr_node.data
        ls = self.maxPathSum(curr_node.left, maxSum)
        rs = self.maxPathSum(curr_node.right, maxSum)
        totalSum = ls + rs + curr_node.data
        #print(maxSum[0], "***************")
        maxSum[0] = max(maxSum[0], totalSum)
        #print(maxSum[0])
        return max(ls, rs) + curr_node.data

    def rootToLeafSum(self, curr_node, totalSum, stack=[]):
        if curr_node is None:
            return 0
        stack.append(curr_node.data)

        self.rootToLeafSum(curr_node.left, totalSum, stack)

        if curr_node.left is None and curr_node.right is None:
            #print("total sum",totalSum)

            i = 0
            #print(stack)
            for x in stack[::-1]:
                totalSum[0] = totalSum[0] + x*(10**i)
                i += 1
            #print(totalSum)
            #return totalSum

        self.rootToLeafSum(curr_node.right,totalSum,stack)
        #print("left and right completed so deleting last element from stack:",stack[-1])
        stack.pop()
        #,return totalSum

    def rootToLeafIterative(self,curr_node):
        if curr_node is None:
            return None
        stack = []
        list_node = []
        totalSum = 0
        stack.append(curr_node)
        while stack:
            curr_node = stack.pop()
            if curr_node.left is not None:
                list_node.append(curr_node.data)
                stack.append(curr_node.left)
            elif curr_node.right is not None:
                list_node.append(curr_node.data)
                stack.append(curr_node.right)
            else:
                i = 0
                for x in list_node[::-1]:
                    totalSum = totalSum + x * (10 ** i)
                    i += 1
                stack.pop()
        return totalSum


    def buildTree(self,inOrder,preOrder,inS,inE,i):

        if inS > inE:
            print("got into breaking condition")
            return None
        tNode = Node(preOrder[i[0]])
        i[0] += 1
        print(inS, inE,tNode.data)
        if inS == inE:
            print("got into equal ")
            #preOrder = preOrder[1:]
            return tNode
        print(tNode.data,preOrder,inOrder)
        rIndex = self.search(inOrder,tNode.data)
        print(inS,rIndex,inE)
        print("*******************************")
        tNode.left = self.buildTree(inOrder,preOrder,inS,rIndex - 1,i)
        print("*****************************")
        tNode.right = self.buildTree(inOrder,preOrder,rIndex + 1,inE,i)

        return tNode

    def search(self,arr,data):
        for i in range(len(arr)):
            if arr[i] == data:
                return i

    def inOrderTraversal(self,curr_node):
        if curr_node is None:
            return None
        self.inOrderTraversal(curr_node.left)
        print(curr_node.data, end=" ")
        self.inOrderTraversal(curr_node.right)


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
    #maxSum = [-2**32]
    #bst.maxPathSum(bst.root, maxSum)
    #print("maximum sum of a path from one leaf to another in a tree is :",maxSum[0])
    #totalSum = [0]
    #bst.rootToLeafSum(bst.root, totalSum)
    #print("total sum of root to leaf is:",totalSum[0])
    inOrder = [5,6,8,10,11,12,14]
    preOrder = [10,6,5,8,12,11,14]
    i = [0]
    root = bst.buildTree(inOrder,preOrder,0,len(inOrder) - 1,i)
    bst.inOrderTraversal(root)
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def BSTFromArray(self,arr,left,right):
        if left > right:
            return
        if left == right:
            return Node(arr[left])
        mid = (left+right)//2
        new_node = Node(arr[mid])
        new_node.left = self.BSTFromArray(arr,left,mid-1)
        new_node.right = self.BSTFromArray(arr,mid+1,right)
        return new_node

    def printTree(self,root):
        if root is None:
            return
        self.printTree(root.left)
        print(root.data,end= " ")
        self.printTree(root.right)

        return

if __name__ == "__main__":
    arr = [3, 6, 8, 9, 10, 13, 15, 18, 21]
    bst = BST()
    bst.root = bst.BSTFromArray(arr,0,len(arr)-1)
    bst.printTree(bst.root)
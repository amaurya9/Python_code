import collections
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
            print("Node with data already exist")

    def rootToLeafPath(self,curr_node, stack):
        if curr_node is None:
            return None
        stack.append(curr_node.data)
        self.rootToLeafPath(curr_node.left, stack)
        if curr_node.left is None and curr_node.right is None:
            print(*stack)
        self.rootToLeafPath(curr_node.right, stack)
        stack.pop()

    def nodesWithKLeaves(self, curr_node, k):
        if curr_node is None:
            return 0
        if curr_node.left is None and curr_node.right is None:
            return 1
        leftCount = self.nodesWithKLeaves(curr_node.left, k)
        rightCount = self.nodesWithKLeaves(curr_node.right,k)
        totalLeaf = leftCount + rightCount
        if totalLeaf == k:
            print(curr_node.data, end=" ")
        return totalLeaf

    def max_width(self,curr_node):
        if curr_node is None:
            return 0
        queue = []
        queue.append(curr_node)
        max_width = 0
        while queue:
            count = len(queue)
            if count > max_width:
                max_width = count
            while (count > 0):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                count -= 1
        return max_width

    def max_widthArray(self,curr_node):
        if curr_node is None:
            return None
        queue = []
        queue.append(curr_node)
        dict_array = {}
        while queue:
            count = len(queue)
            if dict_array.get(count) is None:
                dict_array[count] = []
            #print(queue)
            dict_array[count].append(list(map(lambda x: x.data, queue)))
            while count > 0:
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                count -= 1
        dict1 = collections.OrderedDict(sorted(dict_array.items(), reverse=1))
        #print(dict1.keys())
        #print(dict1[2])
        for x in dict1[list(dict1.keys())[0]]:
            print (*x)
        #print(dict_array)



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
    stack = []
    #print(" root to leaf path is :")
    #bst.rootToLeafPath(bst.root,stack)

    #print("list of nodes having subtree with k leaf :")
    #bst.nodesWithKLeaves(bst.root,2)

    #print("max width is :",bst.max_width(bst.root))
    bst.max_widthArray(bst.root)
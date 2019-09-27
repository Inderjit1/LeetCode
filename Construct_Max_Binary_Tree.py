from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.top = None

    def constructMaximumBinaryTree(self, nums):
        sortednums = sorted(nums)
        rootvalue = TreeNode(sortednums[-1])
        indexofrootvalue = nums.index(sortednums[-1])

        leftTreeRange, rightTreeRange = nums[:indexofrootvalue], nums[indexofrootvalue+1:]
        leftTreeRange.sort(reverse=True)
        rightTreeRange.sort(reverse=True)
        print(f'leftTreeRange value is: {leftTreeRange}')
        print(f'rightTreeRange is: {rightTreeRange}')

        leftSubTree = self.insert(leftTreeRange)
        self.top = None
        rightSubTree = self.insert(rightTreeRange)

        # print(f'leftSubTree value is: {leftSubTree.left.val}')
        # print(f'rightSubTree is: {rightSubTree.val}')
        # leftSide, rightSide = self.buildRecursiveTree(leftTreeRange), \
        # self.buildRecursiveTree(rightTreeRange)
        rootvalue.left = leftSubTree
        rootvalue.right = rightSubTree

        return rootvalue

    def insert(self, listOfValues):
        for i in listOfValues:
            self.top = self.buildRecursiveTree(self.top, i)
        return self.top
    def buildRecursiveTree(self, node, data):
        if node is None:
            node = TreeNode(data)
        elif data < self.top.val:
            node.left = self.buildRecursiveTree(node.left, data)
        elif data > self.top.val:
            node.right = self.buildRecursiveTree(node.right, data)
        return node


    def print_level_order(self, head, queue=deque()):
        if head is None:
            return
        print (head.val)
        [queue.append(node) for node in [head.left, head.right] if node]
        if queue:
            self.print_level_order(queue.popleft(), queue)





input = [3,2,1,4,6,0,5]
test = Solution()
finishedTree = test.constructMaximumBinaryTree(input)
# test.print_level_order(finishedTree)

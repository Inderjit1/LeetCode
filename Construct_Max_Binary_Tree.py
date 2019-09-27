class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        sortednums = sorted(nums)
        rootvalue = TreeNode(sortednums[-1])
        indexofrootvalue = nums.index(rootvalue)

        leftTreeRange, rightTreeRange = nums[:indexofrootvalue], nums[indexofrootvalue:]
        leftSide, rightSide = self.buildRecursiveTree(leftTreeRange), \
        self.buildRecursiveTree(rightTreeRange)
        rootvalue.left = leftSide
        # rootvalue.right = rightSide

     def buildRecursiveTree(self, listOfValues):
         pass



input = [3,2,1,4,6,0,5]
test = Solution()
print(input.index(6))
test.constructMaximumBinaryTree(input)
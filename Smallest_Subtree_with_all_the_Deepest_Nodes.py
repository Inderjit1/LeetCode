# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    maximum_level = 0
    counter = 0
    def subtreeWithAllDeepest(self, root, max_level, count):
        if root is not None:
            print(root.val)
            counter = self.subtreeWithAllDeepest(root.left, count)
            print("Counter is: {}".format(counter))
            self.subtreeWithAllDeepest(root.right, self.maximum_level)
        else:
            return self.maximum_level
test = Solution()
root = TreeNode(3)
first = TreeNode(5)
second = TreeNode(1)
third = TreeNode(6)
fourth = TreeNode(2)
fifth = TreeNode(0)
sixth = TreeNode(8)
seventh = TreeNode(7)
eigth = TreeNode(4)

root.left, root.right, first.left, first.right = first, second, third, fourth
second.left = fifth
second.right = sixth
fourth.left = seventh
fourth.right = eigth

test.subtreeWithAllDeepest(root, test.maximum_level, count=0)
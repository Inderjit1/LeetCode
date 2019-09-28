class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distributeCoins(self, root):
        pass


test = Solution()
first = TreeNode(1)
second = TreeNode(0)
third = TreeNode(0)
fourth = TreeNode(3)

first.left = second
second.right = fourth
first.right = third
#         1
#     /       \
#    0         0
#      \
#       3
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.numberOfCoins = None

class Solution(object):
    trackingNodesWithCoins = {}
    def distributeCoins(self, root):
        self.findNodeWithMaxCoins(root)

    def findNodeWithMaxCoins(self, root):
        if root is None:
            return

        if root.numberOfCoins == 0:
            self.trackingNodesWithCoins[root.val] = 0
        else:
            self.trackingNodesWithCoins[root.val] = root.numberOfCoins
        if root.left is not None:
            self.findNodeWithMaxCoins(root.left)
        if root.rigth is not None:
            self.findNodeWithMaxCoins(root.left)
test = Solution()
first, second, third, fourth = TreeNode(1), TreeNode(0), TreeNode(0), TreeNode(3)
fourth.numberOfCoins = 4
first.left, second.right, first.right = second, fourth, third
test.distributeCoins(first)
#         1
#     /       \
#    0         0
#      \
#       3


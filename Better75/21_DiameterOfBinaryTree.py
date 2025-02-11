# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return root

        self.maxDiameter = 0

        def dfsHeight(root):
            if root is None:
                return 0

            left = dfsHeight(root.left)
            right = dfsHeight(root.right)

            if left + right > self.maxDiameter:
                self.maxDiameter = left + right

            return max(left, right) + 1

        dfsHeight(root)

        return self.maxDiameter

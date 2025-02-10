class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root == None:
            return None

        buf = root.left
        root.left = root.right
        root.right = buf

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

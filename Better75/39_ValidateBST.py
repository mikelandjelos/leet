class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        def top_down_boundaries(root, left, right):
            if not root:
                return True

            if not (left < root.val < right):
                return False

            left = top_down_boundaries(root.left, left, root.val)
            if not left:
                return False

            right = top_down_boundaries(root.right, root.val, right)
            if not right:
                return False

            return True

        return top_down_boundaries(root, float("-inf"), float("+inf"))

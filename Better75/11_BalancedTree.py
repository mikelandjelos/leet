class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True

        left = self.heightDiff(root.left)
        right = self.heightDiff(root.right)

        return False if left < 0 or right < 0 or abs(left - right) > 1 else True

    def heightDiff(self, root):
        """
        Returns tree height.

        :type root: Optional[TreeNode]
        :rtype: int (height if balanced, -1 if not)
        """
        if root is None:
            return 0

        left = self.heightDiff(root.left)
        right = self.heightDiff(root.right)

        return (
            -1
            if (left < 0 or right < 0 or abs(left - right) > 1)
            else max(left, right) + 1
        )

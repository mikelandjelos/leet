# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.num_of_cameras = 0

        def dfs(node):
            if not node:
                return False, True

            camera, monitored = False, False
            cleft, mleft = dfs(node.left)
            cright, mright = dfs(node.right)

            if cleft or cright:
                monitored = True

            if not mleft or not mright:
                self.num_of_cameras += 1
                camera = True
                monitored = True

            return camera, monitored

        _, monitored = dfs(root)
        return self.num_of_cameras if monitored else self.num_of_cameras + 1

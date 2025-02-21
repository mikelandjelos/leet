# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    raise NotImplemented


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left < right:
            mid = (right + left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

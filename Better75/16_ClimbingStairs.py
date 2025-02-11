class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        curr = 1  # Base case - stair N.
        prev = 1  # Stair N - 1.
        i = 1

        while i < n:
            prevprev = curr + prev  # We are going backwards, i.e. bottom-up.
            curr = prev
            prev = prevprev
            i += 1

        return prev

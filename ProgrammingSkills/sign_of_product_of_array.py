class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        indicator = 0

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                indicator += -1 if indicator == 0 else 1

        return 1 if indicator == 0 else -1

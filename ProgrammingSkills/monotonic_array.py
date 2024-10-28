class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        i = 1
        min_diff = 0
        max_diff = 0

        while i < len(nums):
            diff = nums[i] - nums[i - 1]

            if min_diff > diff:
                min_diff = diff

            if max_diff < diff:
                max_diff = diff

            i += 1

        not_monotonic = min_diff < 0 and max_diff > 0

        return not not_monotonic

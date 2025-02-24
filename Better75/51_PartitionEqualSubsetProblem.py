class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums)
        if target % 2:  # `sum(nums)` is odd.
            return False

        dp = set()
        dp.add(0)
        target //= 2

        for num in nums:  # O(n)
            next_dp = set()
            for t in dp:  # O(sum(nums)/2)
                next_dp.add(t)
                next_dp.add(num + t)
                if num + t == target:
                    return True
            dp = next_dp

        return False

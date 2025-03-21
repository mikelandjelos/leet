class Solution(object):
    def numberOfGoodSubarraySplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        count = 1
        res = 1
        one_spotted = False
        for num in nums:
            if not one_spotted and num == 0:
                continue

            one_spotted = True
            if num == 1:
                res *= count % MOD
                count = 0
            count += 1

        return res % MOD if one_spotted else 0

class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        dp = [-1] * N
        dp[0] = 0

        for i in range(N):  # O(N)
            if dp[i] == -1:
                continue

            for j in range(i + 1, N):  # O(N)
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[-1]

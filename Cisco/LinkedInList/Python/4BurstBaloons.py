class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If `i - 1` or `i + 1` goes out of bounds of the array,
        # then treat it as if there is a balloon with a 1 painted on it.
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[l, r]

            dp[l, r] = 0
            for i in range(l, r + 1):
                dp[l, r] = max(
                    dp[l, r],
                    nums[l - 1] * nums[i] * nums[r + 1] + dfs(l, i - 1) + dfs(i + 1, r),
                )

            return dp[l, r]

        return dfs(1, len(nums) - 2)

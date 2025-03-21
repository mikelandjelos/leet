class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        N = len(nums)
        i = 0
        ans = -1

        for j in range(1, N):
            if nums[j] > nums[i]:
                ans = max(ans, nums[j] - nums[i])
            else:
                i = j

        return ans

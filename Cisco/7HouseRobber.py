class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)

        if N == 1:
            return nums[0]
        if N == 2:
            return max(nums)

        prevprev = 0
        prev = nums[-1]
        cur = nums[-2]

        for i in range(N - 3, -1, -1):
            cur, prev, prevprev = nums[i] + max(prev, prevprev), cur, prev

        return max(cur, prev)

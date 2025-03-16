class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur = res = nums[0]
        for el in nums[1:]:
            cur = max(el, cur + el)
            res = max(res, cur)
        return res

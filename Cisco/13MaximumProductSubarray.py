from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = minprod = res = nums[0]

        for el in nums[1:]:
            if el < 0:
                maxprod, minprod = minprod, maxprod

            maxprod = max(el, maxprod * el)
            minprod = min(el, minprod * el)

            res = max(res, maxprod)

        return res

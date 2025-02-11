class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        result, count = nums[0], 1

        for num in nums[1:]:
            if num == result:
                count += 1
            else:
                if count == 0:
                    result, count = num, 1
                else:
                    count -= 1

        return result

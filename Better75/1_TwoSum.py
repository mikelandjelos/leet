class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        elements = {}

        for index, num in enumerate(nums):
            pair = target - num

            if pair in elements:
                return [elements[pair], index]

            elements[num] = index

        return []

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        count = 0

        for i, num in enumerate(nums):
            if num != 0:
                nums[count] = num
                count += 1

        while count < len(nums):
            nums[count] = 0
            count += 1

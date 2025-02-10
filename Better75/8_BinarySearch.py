class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums)

        while left < right:
            mid = (right + left) / 2
            if target > nums[left]:
                left = mid
            else:
                right = mid

        return -1 if nums[left] != target else left

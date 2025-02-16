class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[left]:  # Left sorted portion.
                if nums[mid] < target or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:  # Right sorted portion.
                if nums[mid] > target or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Step 1: Sort the array
        results = []

        for i, num in enumerate(nums[:-2]):
            if i > 0 and num == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                x = nums[left] + nums[right]
                if x < -num:
                    left += 1
                elif x > -num:
                    right -= 1
                else:
                    results.append([num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1

        return results

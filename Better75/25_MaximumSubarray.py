class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_sum = nums[0]
        prefix_sum = nums[0]

        for num in nums[1:]:
            if prefix_sum < 0:
                prefix_sum = 0

            prefix_sum += num

            if prefix_sum > max_sum:
                max_sum = prefix_sum

        return max_sum

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        subset = []

        def backtracking(i=0):
            if i >= len(nums):
                result.append(subset[::])
                return

            subset.append(nums[i])
            backtracking(i + 1)

            subset.pop()
            backtracking(i + 1)

        backtracking()
        return result

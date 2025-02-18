class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:  # Empty list.
            return [nums]

        base = nums[0]
        perms = self.permute(nums[1:])
        result = []

        for p in perms:
            for i in range(len(p) + 1):
                perm = p[:]
                perm.insert(i, base)
                result.append(perm)

        return result

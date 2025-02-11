class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()

        for number in nums:
            if number in s:
                return True
            s.add(number)

        return False

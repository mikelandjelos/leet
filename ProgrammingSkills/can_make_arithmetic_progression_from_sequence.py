class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        if len(arr) == 1 or len(arr) == 2:
            return True

        arr.sort()

        i = 2
        d = arr[1] - arr[0]

        while i < len(arr):
            if arr[i] - arr[i - 1] != d:
                return False
            i += 1

        return True

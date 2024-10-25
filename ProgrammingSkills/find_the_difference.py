class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        sum_s = sum(ord(ch) for ch in s)
        sum_t = sum(ord(ch) for ch in t)

        return chr(sum_t - sum_s)

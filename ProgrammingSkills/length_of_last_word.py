class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.rstrip()

        for i, letter in enumerate(s[::-1]):
            if letter == " ":
                return i

        return len(s)

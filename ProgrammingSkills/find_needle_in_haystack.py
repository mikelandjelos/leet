class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        i = 0

        while i <= len(haystack) - len(needle):
            j = 0

            while j < len(needle) and haystack[i + j] == needle[j]:
                j += 1

            if j == len(needle):
                return i

            i += 1

        return -1

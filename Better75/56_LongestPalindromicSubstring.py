class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        result_len = 0

        for i, char in enumerate(s):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > result_len:
                    result = s[l : r + 1]
                    result_len = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1  # Even edge case
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > result_len:
                    result = s[l : r + 1]
                    result_len = r - l + 1
                l -= 1
                r += 1

        return result

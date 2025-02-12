class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        substr_chars = set()
        left = 0
        result_length = 0

        for right, char in enumerate(s):
            while char in substr_chars:
                substr_chars.remove(s[left])
                left += 1
            substr_chars.add(char)
            result_length = max(result_length, len(substr_chars))

        return result_length

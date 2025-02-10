import string


class Solution(object):
    def isPalindrome(self, s: str):
        """
        :type s: str
        :rtype: bool
        """
        jump_over = string.whitespace + string.punctuation
        s = s.lower()
        s = s.strip(jump_over)
        i = 0
        j = len(s) - 1

        while i < j:
            while i < len(s) - 1 and s[i] in jump_over:
                i += 1
            while j > 1 and s[j] in jump_over:
                j -= 1

            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_count = {}

        for letter in s:
            if letter not in letter_count:
                letter_count[letter] = 1
                continue

            letter_count[letter] += 1

        length = 0

        for letter, count in letter_count.items():
            if count % 2 == 0:
                length += count
                del letter_count[letter]
            else:
                length += count - 1
                letter_count[letter] -= count - 1

        if len(letter_count) != 0:
            length += 1

        return length

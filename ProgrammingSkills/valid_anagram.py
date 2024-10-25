class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sd = {}

        for letter in s:
            if letter in sd:
                sd[letter] += 1
            else:
                sd[letter] = 1

        for letter in t:
            if letter in sd:
                sd[letter] -= 1

                if sd[letter] == 0:
                    del sd[letter]
            else:
                return False

        return len(sd) == 0

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_lettermap = {}

        for letter in s:
            if letter in s_lettermap:
                s_lettermap[letter] += 1
            else:
                s_lettermap[letter] = 1

        for letter in t:
            if letter in s_lettermap:
                s_lettermap[letter] -= 1
                if s_lettermap[letter] == 0:
                    del s_lettermap[letter]
            else:
                return False

        return len(s_lettermap) == 0

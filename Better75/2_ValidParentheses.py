class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q = []
        d = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for par in s:
            if par in d.values():
                if len(q) > 0 and par == d[q.pop()]:
                    continue
                else:
                    return False

            q.append(par)

        return len(q) == 0

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        index = 0
        if s[0] == "-":
            sign = -1
            index += 1
        elif s[0] == "+":
            index += 1

        result = 0
        while index < len(s) and s[index].isdigit():
            result = result * 10 + (ord(s[index]) - ord("0"))
            index += 1

        result *= sign

        int_min = -(2**31)
        int_max = 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max

        return result

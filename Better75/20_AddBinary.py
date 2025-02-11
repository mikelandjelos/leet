class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = 0
        i = 0

        while i < max(len(a), len(b)):
            frst = ord(a[-i - 1]) - 48 if i < len(a) else 0
            scnd = ord(b[-i - 1]) - 48 if i < len(b) else 0
            sum = frst + scnd + carry
            carry = sum // 2
            result = str(sum % 2) + result
            i += 1

        if carry == 1:
            result = "1" + result

        return result

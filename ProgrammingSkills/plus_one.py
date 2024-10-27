class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        i = len(digits) - 1
        digits[-1] += 1

        while i >= 1:
            if digits[i] >= 10:
                digits[i - 1] += 1
                digits[i] = digits[i] % 10

            i -= 1

        if digits[i] >= 10:
            digits[i] = digits[i] % 10
            digits.insert(0, 1)

        return digits

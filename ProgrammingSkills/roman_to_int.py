class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        jump_next = False
        n = len(s)

        value_translator = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        roman_digit_sum = 0

        for i, roman_digit in enumerate(s):
            if jump_next:
                jump_next = False
                continue

            if i != n - 1 and s[i : i + 2] in value_translator:
                roman_digit_sum += value_translator[s[i : i + 2]]
                jump_next = True
                continue

            roman_digit_sum += value_translator[roman_digit]

        return roman_digit_sum

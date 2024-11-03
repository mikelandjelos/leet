class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        count_5s = 0
        count_10s = 0

        for bill in bills:
            if bill == 5:
                count_5s += 1
            elif bill == 10:
                count_10s += 1
                if count_5s > 0:
                    count_5s -= 1
                else:
                    return False
            elif bill == 20:
                if count_10s > 0 and count_5s > 0:
                    count_5s -= 1
                    count_10s -= 1
                elif count_5s > 2:
                    count_5s -= 3
                else:
                    return False
            else:
                raise ValueError("")

            print(bill)
            print(count_5s)
            print(count_10s)
            print("=============")

        return True

from math import ceil


class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        up_to_low = ceil(low // 2)
        up_to_high = ceil(high // 2)

        return up_to_high - up_to_low

class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        cur_max = values[0]
        max_score = -1

        for el in values[1:]:
            cur_max -= 1
            if cur_max + el > max_score:
                max_score = cur_max + el
            cur_max = max(cur_max, el)

        return max_score

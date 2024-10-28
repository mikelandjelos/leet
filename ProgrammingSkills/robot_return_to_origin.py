class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        left = 0
        up = 0

        for move in moves:
            if move == "L":
                left += 1
            elif move == "R":
                left -= 1
            elif move == "U":
                up += 1
            elif move == "D":
                up -= 1

        return left == 0 and up == 0

import numpy as np


class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """

        table = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        for i, move in enumerate(moves):
            if i % 2 == 0:
                table[tuple(move)] = 1
            else:
                table[tuple(move)] = -1

        # Diagonals.
        if table[0, 0] == 1 and table[1, 1] == 1 and table[2, 2] == 1:
            return "A"
        elif table[0, 0] == -1 and table[1, 1] == -1 and table[2, 2] == -1:
            return "B"

        if table[0, 2] == 1 and table[1, 1] == 1 and table[2, 0] == 1:
            return "A"
        elif table[0, 2] == -1 and table[1, 1] == -1 and table[2, 0] == -1:
            return "B"

        # Horizontal.
        if np.sum(table[0, :]) == 3:
            return "A"
        elif np.sum(table[1, :]) == 3:
            return "A"
        elif np.sum(table[2, :]) == 3:
            return "A"

        if np.sum(table[0, :]) == -3:
            return "B"
        elif np.sum(table[1, :]) == -3:
            return "B"
        elif np.sum(table[2, :]) == -3:
            return "B"

        # Vertical.
        if np.sum(table[:, 0]) == 3:
            return "A"
        elif np.sum(table[:, 1]) == 3:
            return "A"
        elif np.sum(table[:, 2]) == 3:
            return "A"

        if np.sum(table[:, 0]) == -3:
            return "B"
        elif np.sum(table[:, 1]) == -3:
            return "B"
        elif np.sum(table[:, 2]) == -3:
            return "B"

        return "Draw" if len(moves) == 9 else "Pending"

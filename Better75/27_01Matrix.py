from collections import deque


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        if not mat:
            return mat

        q = deque()

        height = len(mat)
        width = len(mat[0])

        for i, row in enumerate(mat):
            for j, el in enumerate(row):
                if el == 0:
                    q.append((i, j))  # Enqueue.
                else:
                    mat[i][j] = -1

        while q:
            row, col = q.popleft()  # Dequeue.
            for drow, dcol in (0, 1), (0, -1), (1, 0), (-1, 0):
                new_row = row + drow
                new_col = col + dcol

                if (
                    0 <= new_row < height
                    and 0 <= new_col < width
                    and mat[new_row][new_col] == -1
                ):
                    mat[new_row][new_col] = mat[row][col] + 1
                    q.append((new_row, new_col))

        return mat

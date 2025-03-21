class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)

        for i in range(N):
            for j in range(i + 1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(N):
            matrix[i].reverse()

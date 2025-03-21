class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        NROWS, NCOLS = len(matrix), len(matrix[0])
        cache = [-1] * NROWS * NCOLS

        def dfs(r, c):
            # Out of bounds.
            if r >= NROWS or c >= NCOLS:
                return 0

            # Already cached.
            if cache[r * NCOLS + c] != -1:
                return cache[r * NCOLS + c]

            cache[r * NCOLS + c] = 0
            right = dfs(r, c + 1)
            diag = dfs(r + 1, c + 1)
            down = dfs(r + 1, c)

            if matrix[r][c] == "1":
                cache[r * NCOLS + c] = 1 + min(right, diag, down)

            return cache[r * NCOLS + c]

        dfs(0, 0)

        return max(cache) ** 2

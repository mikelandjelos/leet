class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # Dimensions.
        m, n = len(matrix), len(matrix[0])

        # Map out indices of zeroes.
        mapped_indices = []
        for i_origin, row in enumerate(matrix):
            for j_origin, element in enumerate(row):
                if element == 0:
                    mapped_indices.append((i_origin, j_origin))

        # Setting zeroes.
        for i_origin, j_origin in mapped_indices:
            # Vertical setting.
            for i in range(0, m):
                matrix[i][j_origin] = 0

            # Horizontal setting.
            for j in range(0, n):
                matrix[i_origin][j] = 0

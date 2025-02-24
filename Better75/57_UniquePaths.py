class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        last_row = [1] * n

        for i in range(m - 2, -1, -1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = last_row[j] + new_row[j + 1]

            last_row = new_row

        return last_row[0]

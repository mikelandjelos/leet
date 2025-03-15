class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        M, N = len(points), len(points[0])

        for i in range(0, M - 1):  # O(M) time
            left2right = [points[i][0]] + [0] * (N - 1)  # O(N) space
            for j in range(1, N):  # O(N) time
                left2right[j] = max(points[i][j], left2right[j - 1] - 1)

            right2left = [0] * (N - 1) + [points[i][-1]]  # O(N) space
            points[i + 1][-1] += max(points[i][-1], left2right[-1], right2left[-1])
            for j in range(N - 2, -1, -1):  # O(N) time
                right2left[j] = max(points[i][j], right2left[j + 1] - 1)
                points[i + 1][j] += max(points[i][j], left2right[j], right2left[j])

        return max(points[-1])

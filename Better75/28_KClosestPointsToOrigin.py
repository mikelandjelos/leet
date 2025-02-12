from heapq import heapify, heappop


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        points = [(x * x + y * y, x, y) for x, y in points]
        heapify(points)  # O(n).

        res = []
        while k > 0:
            res.append(heappop(points)[1:])
            k -= 1
        return res

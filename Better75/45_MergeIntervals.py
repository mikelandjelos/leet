class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda interval: interval[0])  # O(nlogn)
        results = []

        for i, [start, end] in enumerate(intervals[:-1]):
            if end >= intervals[i + 1][0]:
                intervals[i + 1][0], intervals[i + 1][1] = (
                    min(start, intervals[i + 1][0]),
                    max(end, intervals[i + 1][1]),
                )
                continue
            results.append([start, end])

        results.append([intervals[-1][0], intervals[-1][1]])

        return results

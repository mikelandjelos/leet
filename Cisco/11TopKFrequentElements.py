from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        max_freq = max(counts.values())
        reversed_counts = [[] for _ in range(max_freq + 1)]

        for num, count in counts.items():
            reversed_counts[count].append(num)

        res = []
        for i in range(max_freq, 0, -1):
            res.extend(reversed_counts[i])
            if len(res) >= k:
                return res[:k]

from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_rows = set(map(min, matrix))
        max_cols = set(map(max, zip(*matrix)))
        return list(min_rows & max_cols)

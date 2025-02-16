class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtracking(i, cur, total):
            if i >= len(candidates) or total > target:
                return
            if target == total:
                result.append(list(cur))
                return

            cur.append(candidates[i])
            backtracking(i, cur, total + candidates[i])
            cur.pop()  # Very important.
            backtracking(i + 1, cur, total)

        backtracking(0, [], 0)
        return result

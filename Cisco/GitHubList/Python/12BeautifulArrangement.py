class Solution:
    def countArrangement(self, n: int) -> int:
        dp = {}

        def dfs(position, mask):
            if position == 0:
                return 1

            if (position, mask) in dp:
                return dp[position, mask]

            count = 0
            for num in range(1, n + 1):
                if not (mask & (1 << num)) and (
                    num % position == 0 or position % num == 0
                ):
                    count += dfs(position - 1, mask | (1 << num))

            dp[position, mask] = count
            return count

        return dfs(n, 0)

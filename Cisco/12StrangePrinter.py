class Solution:
    def strangePrinter(self, s: str) -> int:
        N = len(s)
        INF = 101
        dp = [[INF] * N for i in range(N)]

        dp[-1][-1] = 1  # Last letter substring.

        for i in range(N - 2, -1, -1):  # O(N)
            dp[i][i] = 1

            for j in range(i + 1, N):  # O(N)
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]  # This is because of the overwriting :)
                else:
                    for k in range(i, j):
                        dp[i][j] = min(
                            dp[i][j],
                            dp[i][k] + dp[k + 1][j],
                        )

        return dp[0][-1]

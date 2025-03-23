#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    int strangePrinter(string s)
    {
        int N = s.size();
        vector<vector<int>> dp(N, vector<int>(N, 101));

        for (int i = N - 1; i >= 0; --i)
        {
            dp[i][i] = 1;
            for (int j = i + 1; j < N; ++j)
            {
                if (s[i] == s[j])
                {
                    dp[i][j] = dp[i][j - 1];
                    continue;
                }

                for (int k = i; k < j; ++k)
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j]);
            }
        }

        return dp[0][N - 1];
    }
};
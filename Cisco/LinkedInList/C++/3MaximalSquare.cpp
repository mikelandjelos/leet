    #include <vector>
    #include <algorithm>

    using namespace std;

    class Solution
    {
    public:
        int maximalSquare(vector<vector<char>> &matrix)
        {
            int M = matrix.size(), N = matrix[0].size();
            if (M == 0 || N == 0)
                return 0;

            vector<vector<int>> dp(M, vector<int>(N, 0));
            int maxSquare = 0;

            for (int i = 0; i < M; ++i)
                for (int j = 0; j < N; ++j)
                    if (matrix[i][j] == '1')
                    {
                        if (i == 0 || j == 0)
                            dp[i][j] = 1;
                        else
                            dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});

                        maxSquare = max(maxSquare, dp[i][j]);
                    }

            return maxSquare * maxSquare;
        }
    };

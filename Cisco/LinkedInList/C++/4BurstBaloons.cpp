#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int maxCoins(vector<int> &nums)
    {
        int N = nums.size();
        vector<vector<int>> dp = vector(N + 2, vector<int>(N + 2, 0));

        nums.insert(nums.begin(), 1);
        nums.insert(nums.end(), 1);

        for (int r = 1; r <= N; ++r)
            for (int l = r; l >= 1; --l)
                for (int k = l; k <= r; ++k)
                    dp[l][r] = max(dp[l][r], nums[l - 1] * nums[k] * nums[r + 1] +
                                                 dp[l][k - 1] + dp[k + 1][r]);

        return dp[1][N];
    }
};
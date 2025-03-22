#include <vector>
#include <cmath>

using namespace std;

class Solution
{
public:
    int maximumJumps(vector<int> &nums, int target)
    {
        int N = nums.size();
        vector<int> dp(N, -1);

        dp[0] = 0;

        for (int i = 0; i < N; ++i)
        {
            if (dp[i] == -1)
                continue;

            for (int j = i + 1; j < N; ++j)
                if (target >= abs(nums[j] - nums[i]))
                    dp[j] = max(dp[j], dp[i] + 1);
        }

        return dp[N - 1];
    }
};
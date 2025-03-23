#include <vector>

using namespace std;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int curr = nums[0], maxSum = nums[0], N = nums.size();

        for (int i = 1; i < N; ++i)
            curr = max(curr + nums[i], nums[i]),
            maxSum = max(maxSum, curr);

        return maxSum;
    }
};
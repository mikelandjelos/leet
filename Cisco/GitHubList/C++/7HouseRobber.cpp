#include <vector>

using namespace std;

class Solution
{
public:
    int rob(vector<int> &nums)
    {
        int N = nums.size();
        if (N == 1)
            return nums[0];
        if (N == 2)
            return max(nums[0], nums[1]);

        int prev = nums[N - 2],
            prevprev = nums[N - 1],
            prevprevprev = 0;
        int cur;

        for (int i = N - 3; i >= 0; --i)
            cur = nums[i] + max(prevprev, prevprevprev),
            prevprevprev = prevprev,
            prevprev = prev,
            prev = cur;

        return max(prev, prevprev);
    }
};
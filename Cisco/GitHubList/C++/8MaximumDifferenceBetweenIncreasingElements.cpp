#include <vector>

using namespace std;

class Solution
{
public:
    int maximumDifference(vector<int> &nums)
    {
        int iMin = 0, N = nums.size(), result = -1;
        for (int i = 1; i < N; ++i)
        {
            if (nums[i] > nums[iMin])
                result = max(result, nums[i] - nums[iMin]);
            else
                iMin = i;
        }
        return result;
    }
};
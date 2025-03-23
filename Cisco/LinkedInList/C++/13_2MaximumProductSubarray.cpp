#include <vector>

using namespace std;

class Solution
{
public:
    int maxProduct(vector<int> &nums)
    {
        int currMax = nums[0], currMin = nums[0], globMax = nums[0];

        for (int i = 1; i < nums.size(); ++i)
        {
            if (nums[i] < 0)
                swap(currMax, currMin);

            currMax = max(nums[i], nums[i] * currMax);
            currMin = min(nums[i], nums[i] * currMin);
            globMax = max(globMax, currMax);
        }

        return globMax;
    }
};
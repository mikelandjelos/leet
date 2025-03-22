#include <vector>
#include <cmath>

using namespace std;

class Solution
{
public:
    int numberOfGoodSubarraySplits(vector<int> &nums)
    {
        int N = nums.size(), firstOneIndex = -1;
        for (size_t i = 0; i < nums.size(); ++i)
            if (nums[i] == 1)
            {
                firstOneIndex = i;
                break;
            }

        if (firstOneIndex == -1)
            return 0;

        unsigned long numberOfWays = 1, MOD = 1'000'000'007, count = 1;
        for (size_t i = firstOneIndex + 1; i < nums.size(); ++i)
        {
            if (nums[i] == 1)
            {
                numberOfWays = (numberOfWays * count) % MOD;
                count = 1;
                continue;
            }
            count++;
        }

        return numberOfWays;
    }
};
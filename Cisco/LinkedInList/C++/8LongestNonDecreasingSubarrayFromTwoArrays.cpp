#include <vector>

using namespace std;

class Solution
{
public:
    int maxNonDecreasingLength(vector<int> &nums1, vector<int> &nums2)
    {
        int N = nums1.size(), curr1, curr2, prev1 = 1, prev2 = 1, best = 1;

        for (int i = 1; i < N; ++i)
        {
            curr1 = 1, curr2 = 1;

            if (nums1[i] >= nums1[i - 1])
                curr1 = prev1 + 1;
            if (nums1[i] >= nums2[i - 1])
                curr1 = max(curr1, prev2 + 1);

            if (nums2[i] >= nums1[i - 1])
                curr2 = prev1 + 1;
            if (nums2[i] >= nums2[i - 1])
                curr2 = max(curr2, prev2 + 1);

            prev1 = curr1, prev2 = curr2, best = max(best, max(curr1, curr2));
        }

        return best;
    }
};
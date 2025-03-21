#include <vector>

using namespace std;

class Solution
{
public:
    int numFriendRequests(vector<int> &ages)
    {
        vector<int> ageGroups(121, 0);
        for (auto &age : ages) // O(N)
            ageGroups[age] += 1;

        int requestCount = 0;
        for (int x = 0; x < ageGroups.size(); ++x) // O(1)
            for (int y = 0; y < ageGroups.size(); ++y) // O(1)
            {
                if (y <= x && y > 0.5 * x + 7)
                {

                    requestCount += ageGroups[x] * ageGroups[y];
                    if (x == y)
                        requestCount -= ageGroups[x];
                }
            }

        return requestCount;
    }
};
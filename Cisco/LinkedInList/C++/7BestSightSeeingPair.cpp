#include <vector>
#include <span>

using namespace std;

class Solution
{
public:
    int maxScoreSightseeingPair(vector<int> &values)
    {
        int N = values.size();
        int currMax = values[0], maxScore = -1;
        for (int i = 1; i < N; ++i)
        {
            currMax -= 1;
            maxScore = max(maxScore, currMax + values[i]);
            currMax = max(currMax, values[i]);
        }

        return maxScore;
    }
};
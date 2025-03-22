#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    long long maxPoints(vector<vector<int>> &points)
    {
        int M = points.size(), N = points[0].size();

        vector<long long> left2right(N, 0), right2left(N, 0), current(points[0].begin(), points[0].end());

        for (int i = 1; i < M; ++i)
        {
            left2right[0] = current[0];
            for (int j = 1; j < N; ++j)
                left2right[j] = max(left2right[j - 1] - 1, current[j]);

            right2left[N - 1] = current[N - 1];
            for (int j = N - 2; j >= 0; --j)
                right2left[j] = max(right2left[j + 1] - 1, current[j]);

            for (int j = 0; j < N; ++j)
                current[j] = points[i][j] + max(left2right[j], right2left[j]);
        }

        return *max_element(current.begin(), current.end());
    }
};

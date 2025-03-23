#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<int> luckyNumbers(vector<vector<int>> &matrix)
    {
        const int M = matrix.size();
        const int N = matrix[0].size();
        vector<int> minRows(M, 100001);
        vector<int> maxCols(N, -1);
        vector<int> luckyNumbers;

        for (int i = 0; i < M; ++i)
            for (int j = 0; j < N; ++j)
                minRows[i] = min(minRows[i], matrix[i][j]),
                maxCols[j] = max(maxCols[j], matrix[i][j]);

        for (int i = 0; i < M; ++i)
            for (int j = 0; j < N; ++j)
                if (matrix[i][j] == minRows[i] && matrix[i][j] == maxCols[j])
                    luckyNumbers.push_back(matrix[i][j]);

        return luckyNumbers;
    }
};
#include <vector>
#include <queue>

using namespace std;

class Solution
{
public:
    int maxCandies(vector<int> &status, vector<int> &candies,
                   vector<vector<int>> &keys, vector<vector<int>> &containedBoxes, vector<int> &initialBoxes)
    {
        int NUM_BOXES = status.size();
        queue<int> q;
        vector<bool> reachableClosed(NUM_BOXES, false);

        for (const auto &box : initialBoxes)
            if (status[box])
                q.push(box);
            else
                reachableClosed[box] = true;

        int candiesCollected = 0;
        while (!q.empty())
        {
            int box = q.front();
            q.pop();
            candiesCollected += candies[box];

            for (const auto &key : keys[box])
            {
                if (!status[key] && reachableClosed[key])
                    q.push(key);
                status[key] = 1; // Reachable or not - unlocking it (this is neat trick) :)
            }

            for (const auto &containedBox : containedBoxes[box])
                if (status[containedBox])
                    q.push(containedBox);
                else
                    reachableClosed[containedBox] = true;
        }

        return candiesCollected;
    }
};
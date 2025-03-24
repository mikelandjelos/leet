#include <vector>
#include <queue>
#include <limits.h>
#include <algorithm>

using namespace std;

template <typename T>
using MinHeap = priority_queue<T, vector<T>, greater<T>>;

class Solution
{
public:
    int networkDelayTime(vector<vector<int>> &times, int n, int k)
    {
        vector<vector<pair<int, int>>> graph(n);

        for (const auto &edge : times)
            graph[edge[0] - 1].emplace_back(edge[1] - 1, edge[2]);

        MinHeap<pair<int, int>> pq;
        vector<int> distances(n, INT_MAX);
        
        pq.emplace(0, k - 1);
        distances[k - 1] = 0;

        while (!pq.empty())
        {
            auto [timeToCurrent, current] = pq.top();
            pq.pop();

            if (timeToCurrent > distances[current])
                continue;

            for (const auto &[neighbor, distanceToNeighbor] : graph[current])
            {
                int timeToNeighbor = timeToCurrent + distanceToNeighbor;
                if (timeToNeighbor >= distances[neighbor])  
                    continue;
                
                distances[neighbor] = timeToNeighbor;
                pq.emplace(timeToNeighbor, neighbor);
            }
        }

        int maxTime = *max_element(distances.begin(), distances.end());
        return maxTime == INT_MAX ? -1 : maxTime;
    }
};

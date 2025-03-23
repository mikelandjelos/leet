#include <vector>
#include <queue>
#include <algorithm>
#include <limits.h>

using namespace std;

template <typename T, typename Compare = greater<T>>
using Heap = priority_queue<T, vector<T>, Compare>;

template <typename T>
using MaxHeap = Heap<T, less<T>>;

template <typename T>
using MinHeap = Heap<T, greater<T>>;

class Solution
{
public:
    int networkDelayTime(vector<vector<int>> &times, int n, int k)
    {
        vector<vector<pair<int, int>>> graph(n);

        for (const auto &edge : times)
            graph[edge[0] - 1].emplace_back(edge[1] - 1, edge[2]);

        MinHeap<pair<int, int>> pq;
        pq.emplace(0, k - 1);

        vector<int> dist(n, INT_MAX);
        dist[k - 1] = 0;

        while (!pq.empty()) // O((V+E) log V)
        {
            auto [time, node] = pq.top();
            pq.pop();

            if (time > dist[node])
                continue;

            for (const auto &[neighbor, weight] : graph[node])
            {
                int newTime = time + weight;
                if (newTime < dist[neighbor])
                {
                    dist[neighbor] = newTime;
                    pq.emplace(newTime, neighbor);
                }
            }
        }

        int maxTime = *max_element(dist.begin(), dist.end());
        return maxTime == INT_MAX ? -1 : maxTime;
    }
};

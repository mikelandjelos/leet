#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> counter;
        for (const auto &num : nums)
            counter[num]++;

        priority_queue<pair<int, int>, vector<pair<int, int>>, less<>> maxHeap;

        for (const auto &[num, count] : counter)
            maxHeap.emplace(count, num);

        vector<int> result;
        for (int i = 0; i < k; ++i)
            result.push_back(maxHeap.top().second), maxHeap.pop();

        return result;
    }
};
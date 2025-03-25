#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
    bool isStretchy(const string &base, const string &query)
    {
        int basePtr = 0, queryPtr = 0;

        while (basePtr < base.size() && queryPtr < query.size())
        {
            if (base[basePtr] != query[queryPtr])
                return false;

            int countBase = 1;
            while (basePtr + 1 < base.size() && base[basePtr] == base[basePtr + 1])
                ++countBase, ++basePtr;

            int countQuery = 1;
            while (queryPtr + 1 < query.size() && query[queryPtr] == query[queryPtr + 1])
                ++countQuery, ++queryPtr;

            if (countBase < 3 && countBase != countQuery)
                return false;
            if (countQuery > countBase)
                return false;

            ++basePtr, ++queryPtr;
        }

        return basePtr == base.size() && queryPtr == query.size();
    }

public:
    int expressiveWords(string s, vector<string> &words)
    {
        return count_if(words.begin(), words.end(), [&](const string &queryStr)
                        { return isStretchy(s, queryStr); });
    }
};

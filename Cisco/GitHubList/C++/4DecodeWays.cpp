#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    int numDecodings(string s)
    {
        int N = s.size();
        const auto &isValid = [&](const char &curr, const char &prev = 0)
        {
            if (prev != 0)
                return curr == '1' or (curr == '2' and prev >= '0' and prev <= '6');
            return curr != '0';
        };

        int p = s[N - 1] != '0' ? 1 : 0, pp = 1;
        for (int i = N - 2; i >= 0; --i)
        {
            int c = 0;
            if (isValid(s[i]))
                c += p;
            if (isValid(s[i], s[i + 1]))
                c += pp;

            pp = p, p = c;
        }

        return p;
    }
};
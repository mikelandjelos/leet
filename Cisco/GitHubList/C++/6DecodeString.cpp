#include <string>
#include <stack>

using namespace std;

class Solution
{
public:
    string decodeString(string s)
    {
        stack<int> multiplierStack;
        stack<string> substringStack;
        string currSubstr;
        int currMultiplier;

        for (const auto &ch : s)
            if (isalpha(ch))
                currSubstr += ch;
            else if (isdigit(ch))
                currMultiplier = currMultiplier * 10 + (ch - '0');
            else if (ch == '[')
            {
                multiplierStack.push(currMultiplier), currMultiplier = 0;
                substringStack.push(currSubstr), currSubstr = "";
            }
            else // ch == ']'
            {
                string temp = currSubstr;
                currSubstr = substringStack.top(), substringStack.pop();
                currMultiplier = multiplierStack.top(), multiplierStack.pop();

                while (currMultiplier)
                {
                    currSubstr += temp;
                    --currMultiplier;
                }
            }

        return currSubstr;
    }
};
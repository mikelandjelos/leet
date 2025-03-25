#include <string>
#include <stack>

using namespace std;

class Solution
{
    constexpr char getBackward(char forward)
    {
        switch (forward)
        {
        case ')':
            return '(';
        case '}':
            return '{';
        case ']':
            return '[';
        default:
            return '\000';
        }
    }

public:
    bool isValid(string s)
    {
        stack<char> parentheses;

        for (const auto &ch : s)
            if (ch == ')' || ch == '}' || ch == ']')
                if (parentheses.size() == 0 || getBackward(ch) != parentheses.top())
                    return false;
                else
                    parentheses.pop();
            else
                parentheses.push(ch);

        return parentheses.size() == 0;
    }
};
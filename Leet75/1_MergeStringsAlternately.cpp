#include <string>

class Solution
{
public:
    std::string mergeAlternately(std::string word1, std::string word2)
    {
        std::string result;
        int i = 0;
        int minLen = std::min(word1.length(), word2.length());

        while (i < minLen)
            result += word1[i],
            result += word2[i++];

        while (i < word1.length())
            result += word1[i++];

        while (i < word2.length())
            result += word2[i++];

        return result;
    }
};
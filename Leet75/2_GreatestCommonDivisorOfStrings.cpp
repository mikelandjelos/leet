#include <string>

class Solution
{
public:
    std::string gcdOfStrings(std::string str1, std::string str2)
    {
        int minLen = std::min(str1.length(), str2.length());
        int maxLen = std::max(str1.length(), str2.length());
        int lengthOfGCD = 0;
        
        for (int i = 1; i <= minLen && str1[i - 1] == str2[i - 1]; ++i)
            if (minLen % i == 0 && maxLen % i == 0)
                lengthOfGCD = i;

        for (int i = lengthOfGCD; i < maxLen; ++i)
        {
        }

        std::string gcd = "";
        for (int i = 0; i < lengthOfGCD; ++i)
            gcd += str1[i];
        
        return gcd;
    }
};
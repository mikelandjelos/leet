class Solution
{
public:
    int hammingWeight(int n)
    {
        int numOf1Bits = 0;
        while (n > 0)
            numOf1Bits += n & 1, n >>= 1;
        return numOf1Bits;
    }
};
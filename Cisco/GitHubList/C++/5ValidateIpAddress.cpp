#include <string>
#include <vector>

using namespace std;

class Solution
{
    bool isValidIPv4(const string &ip)
    {
        vector<string> segments;
        size_t start = 0, end;
        while ((end = ip.find('.', start)) != string::npos)
        {
            segments.push_back(ip.substr(start, end - start));
            start = end + 1;
        }
        segments.push_back(ip.substr(start));

        if (segments.size() != 4)
            return false;

        for (const string &segment : segments)
        {
            if (segment.empty() || segment.size() > 3)
                return false;

            if (segment.size() > 1 && segment[0] == '0')
                return false;

            for (char ch : segment)
                if (!isdigit(ch))
                    return false;

            int num = stoi(segment);
            if (num < 0 || num > 255)
                return false;
        }
        return true;
    }

    bool isValidIPv6(const string &ip)
    {
        vector<string> segments;
        size_t start = 0, end;
        while ((end = ip.find(':', start)) != string::npos)
        {
            segments.push_back(ip.substr(start, end - start));
            start = end + 1;
        }
        segments.push_back(ip.substr(start));

        if (segments.size() != 8)
            return false;

        for (const string &segment : segments)
        {
            if (segment.empty() || segment.size() > 4)
                return false;

            for (char ch : segment)
                if (!isxdigit(ch))
                    return false;
        }
        return true;
    }

public:
    string validIPAddress(string queryIP)
    {
        if (queryIP.find('.') != string::npos)
            return isValidIPv4(queryIP) ? "IPv4" : "Neither";
        if (queryIP.find(':') != string::npos)
            return isValidIPv6(queryIP) ? "IPv6" : "Neither";
        return "Neither";
    }
};
